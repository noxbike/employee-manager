# 🧑‍💼 Employee Manager

**Employee Manager** is a web application built with **Django** that allows you to manage employees  
(create, view, update, and delete).

The project uses **DaisyUI (Tailwind CSS)** for a modern user interface and is fully **dockerized**
with **Docker** and **Docker Compose** for easy setup and deployment.

---

## 🚀 Features

- ➕ Add an employee
- 📋 List employees
- ✏️ Update employee information
- 🗑️ Delete an employee with confirmation
- 🎨 Modern UI with DaisyUI
- 🐳 Ready-to-use Docker environment

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (Django built-in database)
- **Frontend**: Django Templates + Tailwind CSS + DaisyUI
- **Containerization**: Docker & Docker Compose

---

## 📂 Project Structure

```bash
.
├── app/
│   ├── employee_manager/
│   ├── employee_manager_project/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── manage.py
├── docker-compose.yml
└── README.md

⚙️ Prerequisites

Before you begin, make sure you have installed:

Docker

Docker Compose

▶️ Run the project with Docker
1️⃣ Clone the repository
git clone https://github.com/your-username/employee-manager.git
cd employee-manager

2️⃣ Build the Docker images
docker-compose build

3️⃣ Start the application
docker-compose up

🌐 Access the application

Once the containers are running, open your browser and go to:

http://localhost:8000

🗄️ Django migrations

Apply migrations:

docker-compose exec web python manage.py migrate


Create a superuser:

docker-compose exec web python manage.py createsuperuser

🎨 User Interface

The UI is built with DaisyUI, based on Tailwind CSS, providing:

a clean and modern design

reusable UI components

good responsiveness on desktop and mobile devices

🔐 Security & Best Practices

CSRF protection enabled

Safe delete actions using POST requests

Clear separation between views, templates, and business logic

📌 Possible Improvements

🔐 Authentication and role management

🗃️ Migration to PostgreSQL

🔍 Search and pagination

🚀 Production deployment (VPS, Railway, Render, etc.)

👨‍💻 Author

Developed by Mickaël Morel
💼 Web Developer (Django / Docker / Modern Frontend)
🌍 Open to international projects
