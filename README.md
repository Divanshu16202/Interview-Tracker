# 🚀 Interview Tracker (Django Project)

A powerful **Interview Preparation & Tracking System** built using Django.
This project helps students prepare for technical interviews by practicing coding questions, taking mock tests, and generating AI-based interview questions.

---

## 📌 Features

### 🧠 AI Mock Interview Generator

* Generate interview questions using **Gemini AI API**
* Select category (DSA, DBMS, OS, etc.)
* Choose difficulty level (Easy, Medium, Hard)
* Automatically stores generated questions

### 📝 Mock Interview System

* Attempt predefined mock tests
* Get instant score after submission
* Track your performance

### 💻 Coding Practice Tracker

* Add coding problems you practiced
* Update or delete entries
* Maintain daily practice log

### 🔥 Streak System

* Track your daily coding streak
* Stay consistent with preparation

### 🔐 Authentication System

* User registration & login
* Secure logout functionality
* Personalized dashboard

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **AI Integration:** Google Gemini API
* **Authentication:** Django Auth System

---

## 📂 Project Structure

```
interview_tracker/
│
├── tracker/                # Main app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   └── migrations/
│
├── interview_tracker/      # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/interview-tracker.git
cd interview-tracker
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file and add:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Migrations

```
python manage.py migrate
```

### 6️⃣ Start Server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 📸 Screens (Optional)

* Dashboard
* AI Mock Generator
* Coding Tracker
* Mock Test Page

*(Add screenshots here for better presentation)*

---

## 🔐 Security Notes

* Do NOT expose:

  * Secret Key
  * API Keys
  * Database files
* Use `.env` for sensitive data

---

## 🚀 Future Enhancements

* Leaderboard system
* Performance analytics graphs
* Timer-based mock interviews
* Resume-based AI questions
* Deployment on cloud (Render)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make changes
4. Submit a pull request

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Divanshu Marwaha**
Full Stack Developer

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* Share with others
* Improve your interview prep 🚀

---
