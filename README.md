# Django Todo API with Docker & MySQL

This is a simple **Django REST Framework (DRF)** project that provides a Todo API.  
It runs on **Docker** with a **MySQL database**.

---

## 🚀 Features
- Django 5 + DRF
- MySQL database
- Dockerized setup
- API endpoints for managing Todo items

---

## 📦 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/demodjango.git
cd demodjango

### 2. Create .env file
```bash
MYSQL_DATABASE=demodjango
MYSQL_USER=demouser
MYSQL_PASSWORD=demopassword
MYSQL_ROOT_PASSWORD=rootpassword
SECRET_KEY=your-secret-key
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

### 3. Build & Run with Docker
```bash
docker-compose up --build

### API Endpoints

- GET /api/todoitems/ → List all todos

- POST /api/todoitems/create/ → Create a new todo

- GET /api/todoitems/<id>/ → Retrieve a todo

- PUT /api/todoitems/<id>/update/ → Update a todo

- DELETE /api/todoitems/<id>/delete/ → Delete a todo


