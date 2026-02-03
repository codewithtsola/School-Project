# School Record Management System (Web Application)

Project Overview

The School Record Management System is a web-based application built with Flask and MongoDB, allowing schools to manage student data efficiently. Users can add, view, and update student records securely.

Features:

Add new students (Full Name, Registration Number, Department, Level)

View all students in a dashboard

Responsive design using HTML, CSS, and JavaScript

Flash messages for user feedback

MongoDB for cloud-based storage (Atlas)

Configured for deployment on Vercel

Tech Stack

Backend: Python 3, Flask

Database: MongoDB (Atlas cloud)

Frontend: HTML, CSS, JavaScript, Jinja2 templating

Deployment: Vercel

Setup Instructions

Clone the repo:

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>


Create a virtual environment:

python -m venv .venv
source .venv/Scripts/activate  # Windows
source .venv/bin/activate      # Mac/Linux


Install dependencies:

pip install -r requirements.txt


Set up environment variables:
Create a .env file with:

MONGO_URI=mongodb+srv://<username>:<password>@cluster0.vqirf64.mongodb.net/<dbname>?retryWrites=true&w=majority
FLASK_ENV=development
SECRET_KEY=<your-secret-key>


Run the app locally:

python app.py


Access the app at http://127.0.0.1:5000

Deployment on Vercel

Connect your GitHub repo to Vercel

Add environment variables in Vercel Dashboard:

Key: MONGO_URI
Value: mongodb+srv://<username>:<password>@cluster0.vqirf64.mongodb.net/<dbname>?retryWrites=true&w=majority


Vercel will automatically detect Flask and deploy your app

Access your live app via the Vercel URL

Project Structure
├── app.py                  # Main Flask app
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   └── add_student.html
├── static/                 # CSS and JS files
│   ├── style.css
│   └── script.js
├── requirements.txt        # Dependencies
└── .env                    # Environment variables (not committed)

Future Improvements

User authentication for admin/staff

Edit and delete student records

Advanced filtering by department/level

Export student data to CSV or PDF
## 👥 Default Access

When deployed, anyone with the URL can access the system. For production use, consider adding authentication.
