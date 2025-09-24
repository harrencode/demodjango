# Django Todo API with Next.js Frontend, Docker & MySQL

This is a simple **Django REST Framework (DRF)** project that provides a Todo API with a **Next.js** frontend.  
The backend and frontend are fully **dockerized** and use a MySQL database.

---

## 🚀 Features
- Django 5 + DRF
- Next.js v15.5.4 frontend
- MySQL database
- Dockerized setup
- API endpoints for managing Todo items

---


## 📦 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/harrencode/demodjango.git
cd demodjango
```

### 2. Create .env file
```bash
MYSQL_DATABASE=demodjango
MYSQL_USER=demouser
MYSQL_PASSWORD=demopassword
MYSQL_ROOT_PASSWORD=rootpassword
SECRET_KEY=your-secret-key
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
```

### 3. Build & Run with Docker
```bash
docker-compose up --build
```
### API Endpoints

- GET /api/todoitems/ → List all todos

- POST /api/todoitems/create/ → Create a new todo

- GET /api/todoitems/&lt;id&gt;/ → Retrieve a todo

- PUT /api/todoitems/&lt;id&gt;/ → Update a todo
  
- PATCH /api/todoitems/&lt;id&gt;/  → Partially update a todo (completed toggle)

- DELETE /api/todoitems/&lt;id&gt; → Delete a todo


