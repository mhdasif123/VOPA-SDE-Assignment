# 📚 V-School Assignment API – VOPA SDE Task (Question 1)

This Django REST API allows teachers to assign lessons to individual students, students to view and complete their assignments, and teachers to track assignment completion.

---

## 🚀 Features Implemented

- ✅ Assign a lesson to a student
- ✅ View all incomplete lessons for a student
- ✅ Mark a lesson as completed
- ✅ View all assignments given by a teacher with completion status

---


## 🛠️ Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite3 (default Django DB)

---

## 🗂️ Project Structure

vschool_api/
- ├── assignments/ # App with models, views, serializers, urls
- ├── vschool_api/ # Django settings and main config
- ├── db.sqlite3 # Local test database
- ├── manage.py
- └── README.md

## API Endpoints
Method	      Endpoint	                                                 Description
- POST	       /api/assignments/	                                       - Assign a lesson to a student
- GET	         /api/students/<student_id>/assignments/?status=incomplete - Get student's incomplete lessons
- PUT	         /api/assignments/<assignment_id>/complete/	               - Mark an assignment as complete
- GET	         /api/teachers/<teacher_id>/assignments/status/	           - View all assignments given by teacher


## 🖼️ Screenshots

### Assign Lesson
![Assign](screenshot/Assigment_Lesson.png)

### Student Incomplete Assignments
![Student](screenshots/student_assignments.png)

### Mark as Complete
![Complete](screenshots/mark_complete.png)

### Teacher Assignment Status
![Status](screenshots/teacher_status.png)


---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/YOUR_USERNAME/vopa-sde-assignment.git
cd vopa-sde-assignment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


