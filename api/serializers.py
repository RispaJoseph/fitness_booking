from rest_framework import serializers
from django.utils.timezone import localtime
from .models import FitnessClass, Booking
import pytz

class FitnessClassSerializer(serializers.ModelSerializer):
    local_date_time = serializers.SerializerMethodField()

    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'instructor', 'total_slots', 'available_slots', 'local_date_time']

    def get_local_date_time(self, obj):
        request = self.context.get('request')
        user_tz = request.query_params.get('tz', 'Asia/Kolkata') if request else 'Asia/Kolkata'

        try:
            target_timezone = pytz.timezone(user_tz)
        except Exception:
            target_timezone = pytz.timezone('Asia/Kolkata')

        return localtime(obj.date_time, timezone=target_timezone).strftime('%Y-%m-%d %H:%M:%S')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
