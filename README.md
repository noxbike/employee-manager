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

Docker & Docker Compose (for Docker setup)

Python 3.10+ and pip (for non-Docker setup)

▶️ Run with Docker
1️⃣ Clone the repository
git clone https://github.com/your-username/employee-manager.git
cd employee-manager

2️⃣ Build Docker images
docker-compose build

3️⃣ Start the app
docker-compose up

4️⃣ Open in browser
http://localhost:8000

▶️ Run without Docker
1️⃣ Clone repository & enter app folder
git clone https://github.com/your-username/employee-manager.git
cd employee-manager/app

2️⃣ Create virtual environment
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply migrations
python manage.py migrate

5️⃣ Create superuser (optional)
python manage.py createsuperuser

6️⃣ Start development server
python manage.py runserver

7️⃣ Access in browser
http://127.0.0.1:8000

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
