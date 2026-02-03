# database.py
from pymongo import MongoClient
from student import Student
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

class Database:
    def __init__(self):
        uri = os.getenv("MONGO_URI")
        self.client = MongoClient(uri)
        self.db = self.client["school_db"]
        self.collection = self.db["students"]

    def add_student(self, student):
        # Check if student exists
        if self.collection.find_one({"reg_number": student.reg_number}):
            return False
        self.collection.insert_one(student.to_dict())
        return True

    def get_all_students(self):
        docs = self.collection.find()
        return [Student.from_dict(doc) for doc in docs]

    def get_student(self, reg_number):
        doc = self.collection.find_one({"reg_number": reg_number})
        if doc:
            return Student.from_dict(doc)
        return None

    def search_students(self, query):
        query_lower = query.lower()
        docs = self.collection.find({
            "$or": [
                {"name": {"$regex": query_lower, "$options": "i"}},
                {"reg_number": {"$regex": query_lower, "$options": "i"}},
                {"department": {"$regex": query_lower, "$options": "i"}},
                {"level": {"$regex": query_lower, "$options": "i"}}
            ]
        })
        return [Student.from_dict(doc) for doc in docs]

    def update_student(self, reg_number, updated_student):
        result = self.collection.update_one(
            {"reg_number": reg_number},
            {"$set": updated_student.to_dict()}
        )
        return result.modified_count > 0

    def delete_student(self, reg_number):
        result = self.collection.delete_one({"reg_number": reg_number})
        return result.deleted_count > 0
