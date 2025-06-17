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

<pre> ```plaintext fitness_booking/ ├── api/ │ ├── models.py │ ├── views.py │ ├── serializers.py │ ├── urls.py │ └── ... ├── fitness_booking/ │ ├── settings.py │ ├── urls.py │ └── ... ├── manage.py ├── requirements.txt ├── .gitignore ``` </pre>



