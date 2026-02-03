# app.py
"""
School Record Management System - Web Application
Main Flask application with web interface using MongoDB
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# MongoDB connection
MONGO_URI = os.environ.get(
    "MONGODB_URI",
    "mongodb+srv://tsolapatrick_db_user:PdlTONR1X12A9mmI@cluster0.vqirf64.mongodb.net/?appName=Cluster0"
)
client = MongoClient(MONGO_URI)
db = client.school_db
students_collection = db.students


# Helper functions
def student_to_dict(doc):
    """Convert MongoDB document to student dict"""
    return {
        "name": doc.get("name"),
        "reg_number": doc.get("reg_number"),
        "department": doc.get("department"),
        "level": doc.get("level")
    }


def get_all_students():
    return [student_to_dict(doc) for doc in students_collection.find()]


def get_student(reg_number):
    doc = students_collection.find_one({"reg_number": reg_number})
    return student_to_dict(doc) if doc else None


def add_student(student):
    if students_collection.find_one({"reg_number": student["reg_number"]}):
        return False
    students_collection.insert_one(student)
    return True


def update_student(reg_number, student):
    result = students_collection.update_one(
        {"reg_number": reg_number},
        {"$set": student}
    )
    return result.modified_count > 0


def delete_student(reg_number):
    result = students_collection.delete_one({"reg_number": reg_number})
    return result.deleted_count > 0


def search_students(query):
    docs = students_collection.find({"name": {"$regex": query, "$options": "i"}})
    return [student_to_dict(doc) for doc in docs]


# Routes
@app.route('/')
def index():
    students = get_all_students()
    return render_template('index.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
    if request.method == 'POST':
        student = {
            "name": request.form.get('name', '').strip(),
            "reg_number": request.form.get('reg_number', '').strip(),
            "department": request.form.get('department', '').strip(),
            "level": request.form.get('level', '').strip()
        }

        if not all(student.values()):
            flash('All fields are required!', 'error')
            return redirect(url_for('add_student_route'))

        if add_student(student):
            flash(f"Student {student['name']} added successfully!", 'success')
            return redirect(url_for('index'))
        else:
            flash(f"Registration number {student['reg_number']} already exists!", 'error')
            return redirect(url_for('add_student_route'))

    return render_template('add_student.html')


@app.route('/edit/<reg_number>', methods=['GET', 'POST'])
def edit_student_route(reg_number):
    student = get_student(reg_number)

    if not student:
        flash('Student not found!', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        updated_student = {
            "name": request.form.get('name', '').strip(),
            "reg_number": reg_number,  # cannot change reg_number
            "department": request.form.get('department', '').strip(),
            "level": request.form.get('level', '').strip()
        }

        if not all(updated_student.values()):
            flash('All fields are required!', 'error')
            return redirect(url_for('edit_student_route', reg_number=reg_number))

        if update_student(reg_number, updated_student):
            flash('Student record updated successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Error updating student record!', 'error')

    return render_template('edit_student.html', student=student)


@app.route('/delete/<reg_number>', methods=['POST'])
def delete_student_route(reg_number):
    if delete_student(reg_number):
        flash('Student record deleted successfully!', 'success')
    else:
        flash('Error deleting student record!', 'error')
    return redirect(url_for('index'))


@app.route('/search')
def search_student_route():
    query = request.args.get('q', '').strip()
    if not query:
        return redirect(url_for('index'))

    students = search_students(query)
    if not students:
        flash(f'No students found matching: {query}', 'warning')
    return render_template('index.html', students=students, search_query=query)


@app.route('/api/students')
def api_students():
    students = get_all_students()
    return jsonify(students)


if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
