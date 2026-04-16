# 🎟️ Ticket Booking Management System

A full-featured **Ticket Booking Web Application** built using **Django**, featuring authentication, session-based booking history, and a fully custom admin panel.
This project also incorporates **Docker containerization** and **Jenkins CI/CD pipeline**, demonstrating both backend and DevOps integration.

---

## 🚀 Features

### 👤 Authentication

* Manual user registration and login/logout
* Session-based authentication using Django's built-in system
* No Django Forms (custom implementation)

### 🎫 User Functionality

* View all available shows
* Book tickets with manual HTML form
* Seat quantity selection
* Session-based booking cart
* Booking history page

### 🛠️ Custom Admin Panel

* Add shows manually
* Edit existing shows
* Delete shows
* View all user bookings
* Custom HTML-based admin (No Django Admin used)

---

## 🧑‍💻 Tech Stack

* **Backend:** Django 5.2
* **Frontend:** HTML5, CSS3
* **Database:** SQLite (default Django DB)
* **Containerization:** Docker, Docker Compose
* **CI/CD:** Jenkins Pipeline
* **Version Control:** Git, GitHub

---

## ⚙️ DevOps Setup

### 🐳 Dockerized

* Dockerfile for building Django image
* Python 3.13-slim base image
* docker-compose for service orchestration

### 🛠️ Jenkins CI/CD Pipeline

Multi-stage pipeline includes:

* Install dependencies
* Run tests
* Build container
* Deploy (if configured)

---

## 📂 Project Structure

### Root Directory

```id="dxz4u1"
manage.py
Dockerfile
docker-compose.yml
Jenkinsfile
requirements.txt
```

### config/ (Project Settings)

```id="3q0ycc"
config/
├── settings.py
├── urls.py
└── wsgi.py
```

### booking/ (Main Application)

```id="yq2h0o"
booking/
├── models.py
├── views.py
├── urls.py
└── templates/
```

### Templates

```id="u6yqk8"
templates/booking/
├── show_list.html
├── show_detail.html
├── booking_confirm.html
├── booking_history.html
├── admin_show_list.html
├── admin_add_show.html
├── admin_edit_show.html
├── admin_delete_show.html
└── admin_booking_list.html
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash id="ts8bl6"
git clone https://github.com/Shubham-css/Ticket-Booking-Management-System.git
```

### 2. Navigate to project folder

```bash id="kqg66o"
cd Ticket-Booking-Management-System
```

### 3. Install dependencies

```bash id="s3e9xk"
pip install -r requirements.txt
```

### 4. Run migrations

```bash id="fkgm33"
python manage.py migrate
```

### 5. Run server

```bash id="4z8b0s"
python manage.py runserver
```

---

## 🐳 Run with Docker

```bash id="2f1lkk"
docker-compose up --build
```

---

## 🧠 Key Highlights

* Custom authentication without Django Forms
* Session-based booking system
* Fully custom admin panel
* Dockerized Django application
* Jenkins CI/CD integration
* Clean MVC architecture

---

## 🎯 Use Cases

* Movie ticket booking systems
* Event reservation platforms
* Learning Django backend architecture
* DevOps integration practice

---
🔮 Future Scope

This project lays a strong foundation for a scalable ticket booking system. Several enhancements can be implemented to make it production-ready and more feature-rich:

💳 Payment Integration
Integrate secure online payment gateways (e.g., Stripe, Razorpay)
Enable real-time transaction handling and booking confirmation
🎟️ Seat Selection System
Implement graphical seat layout (like theatres)
Allow users to choose specific seats instead of quantity-based booking
📱 Responsive UI & Frontend Framework
Upgrade frontend using React or Vue.js
Improve UI/UX with fully responsive design for mobile and tablets
📧 Notifications & Alerts
Email/SMS confirmation for bookings
Reminders for upcoming shows
Admin alerts for new bookings
---

## 🔗 Repository Link

https://github.com/Shubham-css/Ticket-Booking-Management-System

---

## 👨‍💻 Author

**Shubham**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
