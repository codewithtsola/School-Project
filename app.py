# app.py
"""
School Record Management System - Web Application
Main Flask application with web interface
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from database import Database
from student import Student
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Initialize database
db = Database()

@app.route('/')
def index():
    """Home page - display all students"""
    students = db.get_all_students()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    """Add new student"""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        reg_number = request.form.get('reg_number', '').strip()
        department = request.form.get('department', '').strip()
        level = request.form.get('level', '').strip()
        
        # Validation
        if not all([name, reg_number, department, level]):
            flash('All fields are required!', 'error')
            return redirect(url_for('add_student'))
        
        student = Student(name, reg_number, department, level)
        
        if db.add_student(student):
            flash(f'Student {name} added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Registration number {reg_number} already exists!', 'error')
            return redirect(url_for('add_student'))
    
    return render_template('add_student.html')

@app.route('/edit/<reg_number>', methods=['GET', 'POST'])
def edit_student(reg_number):
    """Edit existing student"""
    student = db.get_student(reg_number)
    
    if not student:
        flash('Student not found!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        department = request.form.get('department', '').strip()
        level = request.form.get('level', '').strip()
        
        if not all([name, department, level]):
            flash('All fields are required!', 'error')
            return redirect(url_for('edit_student', reg_number=reg_number))
        
        updated_student = Student(name, reg_number, department, level)
        
        if db.update_student(reg_number, updated_student):
            flash('Student record updated successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Error updating student record!', 'error')
    
    return render_template('edit_student.html', student=student)

@app.route('/delete/<reg_number>', methods=['POST'])
def delete_student(reg_number):
    """Delete student"""
    if db.delete_student(reg_number):
        flash('Student record deleted successfully!', 'success')
    else:
        flash('Error deleting student record!', 'error')
    
    return redirect(url_for('index'))

@app.route('/search')
def search_student():
    """Search for student"""
    query = request.args.get('q', '').strip()
    
    if not query:
        return redirect(url_for('index'))
    
    student = db.get_student(query)
    students = [student] if student else []
    
    if not student:
        flash(f'No student found with registration number: {query}', 'warning')
    
    return render_template('index.html', students=students, search_query=query)

@app.route('/api/students')
def api_students():
    """API endpoint to get all students as JSON"""
    students = db.get_all_students()
    return jsonify([student.to_dict() for student in students])

if __name__ == '__main__':
    # Create templates folder if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    # Run the application
    # For development
    app.run(debug=True, host='0.0.0.0', port=5000)
    
    # For production, use:
    # app.run(host='0.0.0.0', port=5000)