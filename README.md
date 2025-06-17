#  Fitness Booking API

This is a RESTful API for a fictional fitness studio built using Django and Django REST Framework. It allows users to view upcoming classes and book slots.

---

## 📌 Features

- View all upcoming fitness classes
- Book a class by providing name and email
- Prevents overbooking by tracking available slots
- Retrieve all bookings by client email
- Automatically filters past classes

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/RispaJoseph/fitness_booking.git
cd fitness_booking
```

### 2. Install dependencies

```bash
pip install django djangorestframework
```

### 3. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Start the server

```bash
python manage.py runserver
```

---

## 📬 API Endpoints

### ✅ View all upcoming classes

**GET** `/api/classes/`

Returns a list of upcoming classes ordered by date and time.

### ✅ Book a class

**POST** `/api/book/`

**Request Body:**

```bash
{
  "class_id": 3,
  "client_name": "Sara",
  "client_email": "sara@gmail.com"
}
```

**Successful Response Example:**

```bash
{
  "id": 1,
  "fitness_class": 3,
  "client_name": "Sara",
  "client_email": "sara@gmail.com"
}
```

**If slots are full:**

```bash
{
  "error": "No slots available"
}
```

### ✅ Get bookings by email

**GET** `/api/bookings/?email=sara@gmail.com`

Returns all bookings associated with the given email.

---

## 🛠 Built With

* Python 3.10.12
* Django 4.0.3
* Django REST Framework

---

## 📁 Project Structure

## 📁 Project Structure

```
fitness_booking/
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
├── fitness_booking/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3
├── manage.py
├── README.md
```


---

## ✍️ Author

**Rispa Joseph**  
📧 rizpahjoseph@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/rispa-joseph)



