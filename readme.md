# School Record Management System (Web Application)

A web-based student record management system built with Flask and Python.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

### 3. Access the Application

Open your browser and go to:

```
http://localhost:5000
```

## 🌐 Deploying for Remote Access

### Option 1: Deploy to Render (Free & Easy)

1. Create account at [render.com](https://render.com)
2. Create new Web Service
3. Connect your GitHub repository
4. Render will auto-detect Flask and deploy
5. You'll get a URL like: `https://your-app.onrender.com`

### Option 2: Deploy to PythonAnywhere (Free)

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your files
3. Configure Flask app in Web tab
4. Your URL: `https://yourusername.pythonanywhere.com`

### Option 3: Run Locally with ngrok (For Testing)

```bash
# Install ngrok
# Download from https://ngrok.com

# Run your Flask app
python app.py

# In another terminal
ngrok http 5000
```

Your lecturer can access via the ngrok URL (e.g., `https://abc123.ngrok.io`)

## 📱 Features

- ✅ Web-based interface (accessible from any device)
- ✅ Add, view, edit, delete student records
- ✅ Search functionality
- ✅ Responsive design (works on mobile)
- ✅ Real-time validation
- ✅ Beautiful UI

## 🔧 Project Structure

```
school-record-system/
├── app.py                 # Flask application
├── student.py             # Student class
├── database.py            # Database operations
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── add_student.html
│   └── edit_student.html
├── static/                # CSS and JavaScript
│   ├── style.css
│   └── script.js
└── data/
    └── students.json      # Data storage
```

## 👥 Default Access

When deployed, anyone with the URL can access the system. For production use, consider adding authentication.
