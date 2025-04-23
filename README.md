# 🎟️ Ticket Booking Management System

A full-featured ticket booking web application built with Django, featuring authentication, session-based booking history.
A custom admin panel — all strictly adhering to architectural and DevOps constraints.

---

## 🚀 Features

### 👤 Authentication
- Manual user registration & login/logout (no Django Forms)
- Session-based authentication using Django's built-in system

### 🎫 User Functionality
- View all available shows
- Book tickets with manual HTML form (seat quantity selection)
- Session-based booking cart
- Booking history page showing all previous bookings

### 🛠️ Admin Panel (Custom)
- Add/Edit/Delete shows manually
- View all user bookings (stored in DB)
- Fully custom HTML-based admin (no Django Admin used)

---

## 🧑‍💻 Tech Stack

- **Backend**: Django 5.2
- **Frontend**: HTML5 + CSS3
- **Containerization**: Docker, Docker Compose
- **CI/CD**: Jenkins Pipeline
- **Version Control**: Git + GitHub

---

## ⚙️ DevOps Setup

### 🐳 Dockerized
- `Dockerfile` for building the Django image (Python 3.13-slim)
- `docker-compose.yml` for managing Django service

### 🛠️ Jenkins CI/CD Pipeline
- `Jenkinsfile` with multi-stage pipeline:
  - Install dependencies
  - Run tests
    
---

## 📁 Key Project Files


### 📁 Root Directory

- `manage.py`  # Django’s command-line utility for running the project
- `Dockerfile`  # Builds the Docker image for the Django app
- `docker-compose.yml`  # Orchestrates the Django container setup
- `Jenkinsfile`  # Defines CI/CD pipeline stages (build, test, run)
- `requirements.txt`  # Contains all Python dependencies

---

### 📁 config/ (Project Settings)

- `settings.py`  # Django project settings and configurations
- `urls.py`  # Global URL router, includes app-level URLs
- `wsgi.py`  # WSGI entry point for deployment (Gunicorn/Apache)

---

### 📁 booking/ (Main Application)

- `models.py`  # Defines the `Show` and `Booking` data models
- `views.py`  # All logic handled using CBVs (Class-Based Views)
- `urls.py`  # URL patterns mapped to views
- `templates/booking/`
  - `show_list.html`  # Displays all available shows
  - `show_detail.html`  # Show details and booking form
  - `booking_confirm.html`  # Confirmation after booking tickets
  - `booking_history.html`  # Shows user's booking history
  - `admin_show_list.html`  # Admin panel – list of all shows
  - `admin_add_show.html`  # Form to add a new show
  - `admin_edit_show.html`  # Form to edit existing show
  - `admin_delete_show.html`  # Confirmation page to delete show
  - `admin_booking_list.html`  # Admin view for all user bookings
