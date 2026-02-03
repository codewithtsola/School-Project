# database.py
"""
Database module for JSON file operations
Handles all CRUD operations for student records
"""

import json
import os
from student import Student

class Database:
    """
    Database class to manage student records in JSON file
    
    Attributes:
        data_file (str): Path to the JSON data file
    """
    
    def __init__(self, data_file='data/students.json'):
        """
        Initialize the database
        
        Args:
            data_file (str): Path to the JSON file for data storage
        """
        self.data_file = data_file
        self._ensure_data_directory()
        self._ensure_data_file()
    
    def _ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        directory = os.path.dirname(self.data_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
    
    def _ensure_data_file(self):
        """Create data file if it doesn't exist"""
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump([], f)
        else:
            # Verify the file contains valid JSON
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    # If it's not a list, reset it
                    if not isinstance(data, list):
                        with open(self.data_file, 'w') as f:
                            json.dump([], f)
            except json.JSONDecodeError:
                # File is corrupted, reset it
                with open(self.data_file, 'w') as f:
                    json.dump([], f)
    
    def _load_data(self):
        """
        Load student data from JSON file
        
        Returns:
            list: List of student dictionaries
        """
        try:
            with open(self.data_file, 'r') as f:
                content = f.read().strip()
                if not content:  # Empty file
                    return []
                data = json.loads(content)
                # Ensure it's a list
                if not isinstance(data, list):
                    return []
                return data
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading data: {e}")
            return []
    
    def _save_data(self, data):
        """
        Save student data to JSON file
        
        Args:
            data (list): List of student dictionaries
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def add_student(self, student):
        """
        Add a new student to the database
        
        Args:
            student (Student): Student object to add
            
        Returns:
            bool: True if successful, False if registration number exists
        """
        data = self._load_data()
        
        # Debug: Print current data
        print(f"Current data in database: {data}")
        print(f"Trying to add student with reg_number: {student.reg_number}")
        
        # Check if registration number already exists
        for existing_student in data:
            if existing_student.get('reg_number') == student.reg_number:
                print(f"Found duplicate: {existing_student}")
                return False
        
        data.append(student.to_dict())
        result = self._save_data(data)
        print(f"Save result: {result}")
        return result
    
    def get_all_students(self):
        """
        Retrieve all student records
        
        Returns:
            list: List of Student objects
        """
        data = self._load_data()
        return [Student.from_dict(s) for s in data]
    
    def get_student(self, reg_number):
        """
        Get a specific student by registration number
        
        Args:
            reg_number (str): Registration number to search for
            
        Returns:
            Student or None: Student object if found, None otherwise
        """
        data = self._load_data()
        for student_data in data:
            if student_data.get('reg_number') == student.reg_number:
                return Student.from_dict(student_data)
        return None
    
    def update_student(self, reg_number, updated_student):
        """
        Update an existing student record
        
        Args:
            reg_number (str): Registration number of student to update
            updated_student (Student): Updated student object
            
        Returns:
            bool: True if successful, False if student not found
        """
        data = self._load_data()
        
        for i, student_data in enumerate(data):
            if student_data.get('reg_number') == reg_number:
                data[i] = updated_student.to_dict()
                return self._save_data(data)
        
        return False
    
    def delete_student(self, reg_number):
        """
        Delete a student record
        
        Args:
            reg_number (str): Registration number of student to delete
            
        Returns:
            bool: True if successful, False if student not found
        """
        data = self._load_data()
        original_length = len(data)
        
        data = [s for s in data if s.get('reg_number') != reg_number]
        
        if len(data) < original_length:
            return self._save_data(data)
        
        return False
