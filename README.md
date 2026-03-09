# BrightPath - Daycare Management System

BrightPath is a web-based daycare management system designed to help daycare centers manage children, parents, attendance, and daily operations efficiently. The system allows administrators to organize information, track children, and manage communication with parents through a simple and user-friendly interface.

## Features

* Child registration and management
* Parent information management
* Attendance tracking
* Secure authentication and user management
* Organized dashboard for daycare operations
* Responsive user interface

## Tech Stack

Frontend:

* React

Backend:

* Django
* Django REST Framework

Database:

* SQLite (for development)

Tools & Technologies:

* Git & GitHub
* REST APIs
* JSON

## Project Structure

Frontend (React) handles the user interface and communicates with the backend through REST APIs.

Backend (Django + Django REST Framework) manages business logic, authentication, and database operations.

## Installation

### Clone the repository

```
git clone https://github.com/motupams/brightpath.git
cd brightpath
```

### Backend Setup (Django)

```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup (React)

```
cd frontend
npm install
npm start
```

The frontend will run on:

```
http://localhost:3000
```

The backend API will run on:

```
http://127.0.0.1:8000
```

## Future Improvements

* Payment integration for daycare fees
* Parent mobile notifications
* Reports and analytics
* Role-based access control
* Online registration for parents

## Author

Developed by Survive Motupa.

## License

This project is open-source and available for learning and portfolio purposes.

