# student.py
"""
Student class definition
Represents a student record with all required attributes
"""

class Student:
    """
    Student class to represent a student record
    
    Attributes:
        name (str): Full name of the student
        reg_number (str): Unique registration number
        department (str): Student's department
        level (str): Current academic level
    """
    
    def __init__(self, name, reg_number, department, level):
        """
        Initialize a new Student object
        
        Args:
            name (str): Full name of the student
            reg_number (str): Unique registration number
            department (str): Student's department
            level (str): Current academic level
        """
        self.name = name
        self.reg_number = reg_number
        self.department = department
        self.level = level
    
    def to_dict(self):
        """
        Convert student object to dictionary for JSON storage
        
        Returns:
            dict: Dictionary representation of the student
        """
        return {
            'name': self.name,
            'reg_number': self.reg_number,
            'department': self.department,
            'level': self.level
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Student object from a dictionary
        
        Args:
            data (dict): Dictionary containing student data
            
        Returns:
            Student: New Student object
        """
        return cls(
            name=data['name'],
            reg_number=data['reg_number'],
            department=data['department'],
            level=data['level']
        )
    
    def __str__(self):
        """
        String representation of the student
        
        Returns:
            str: Formatted student information
        """
        return (f"Name: {self.name}\n"
                f"Registration Number: {self.reg_number}\n"
                f"Department: {self.department}\n"
                f"Level: {self.level}")
    
    def __repr__(self):
        """
        Developer-friendly representation
        
        Returns:
            str: String representation for debugging
        """
        return f"Student('{self.name}', '{self.reg_number}', '{self.department}', '{self.level}')"