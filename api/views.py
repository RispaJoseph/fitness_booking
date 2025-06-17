import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer

# Create your views here.

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_classes(request):
    logger.info("Fetching all upcoming classes.")
    classes = FitnessClass.objects.filter(date_time__gte=now()).order_by('date_time')
    serializer = FitnessClassSerializer(classes, many=True, context={'request': request})
    logger.debug(f"Classes returned: {serializer.data}")
    return Response(serializer.data)

@api_view(['POST'])
def book_class(request):
    class_id = request.data.get('class_id')
    name = request.data.get('client_name')
    email = request.data.get('client_email')

    logger.info(f"Booking attempt: {email} -> class_id: {class_id}")

    if not all([class_id, name, email]):
        logger.warning("Missing fields in booking request.")
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        fitness_class = FitnessClass.objects.get(id=class_id)
    except FitnessClass.DoesNotExist:
        logger.error(f"Class with ID {class_id} not found.")
        return Response({'error': 'Fitness class not found'}, status=status.HTTP_404_NOT_FOUND)

    if fitness_class.available_slots < 1:
        logger.info(f"No slots available for class ID {class_id}")
        return Response({'error': 'No slots available'}, status=status.HTTP_400_BAD_REQUEST)

    booking = Booking.objects.create(
        fitness_class=fitness_class,
        client_name=name,
        client_email=email
    )
    fitness_class.available_slots -= 1
    fitness_class.save()

    logger.info(f"Booking successful: {booking.client_name} -> class: {fitness_class.name}")
    return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_bookings(request):
    email = request.GET.get('email')
    logger.info(f"Fetching bookings for email: {email}")

    if not email:
        logger.warning("No email provided for booking retrieval.")
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

    bookings = Booking.objects.filter(client_email=email)
    serializer = BookingSerializer(bookings, many=True)
    logger.debug(f"Bookings found: {serializer.data}")
    return Response(serializer.data)