# 🎓 SnapClass — AI-Powered Smart Attendance System

<p align="center">

**Smart • Automated • AI-Powered Classroom Attendance**

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?logo=supabase\&logoColor=white)](https://supabase.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn\&logoColor=white)](https://scikit-learn.org/)

</p>

---

## 📌 About

**SnapClass** is an AI-powered classroom attendance system that automates student attendance using **Face Recognition** and **Voice Recognition**.

Teachers can create subjects, enroll students, and take attendance using classroom images or audio, while students can register, enroll in subjects, and track their attendance.

The application is built with **Python, Streamlit, Computer Vision, Machine Learning, Audio Processing, and Supabase**.

---

## ✨ Key Features

### 👨‍🏫 Teacher

* 🔐 Teacher registration & login
* 📚 Create and manage subjects
* 🔗 Share subject codes
* 📸 Face-based attendance
* 🎙️ Voice-based attendance
* 📊 View attendance results & history

### 👨‍🎓 Student

* 📷 Face-based login
* 📝 Student registration
* 🎙️ Optional voice profile
* 📚 Enroll in subjects
* 📊 Track attendance

### 🤖 AI Features

* Face detection & recognition using **Dlib**
* Face embeddings & similarity matching
* **SVM-based** student identification
* Voice embeddings using **Resemblyzer**
* Audio processing using **Librosa**
* Automated Present/Absent classification

---

## 🔄 How It Works

```text
              ┌─────────────────┐
              │    SnapClass    │
              │  Streamlit App  │
              └────────┬────────┘
                       │
          ┌────────────┴────────────┐
          │                         │
     👨‍🏫 Teacher               👨‍🎓 Student
          │                         │
    Create Subject             Register/Login
          │                         │
    Enroll Students            Join Subject
          │                         │
          └────────────┬────────────┘
                       │
              ┌────────▼────────┐
              │   AI Engine     │
              │                 │
              │ Face Recognition│
              │ Voice Recognition
              └────────┬────────┘
                       │
                Attendance Result
                       │
                ┌──────▼──────┐
                │   Supabase  │
                │   Database  │
                └─────────────┘
```

### 📸 Face Attendance

```text
Classroom Image
      ↓
Face Detection
      ↓
Face Embedding
      ↓
Student Matching
      ↓
Present / Absent
```

### 🎙️ Voice Attendance

```text
Classroom Audio
      ↓
Audio Processing
      ↓
Voice Embedding
      ↓
Speaker Matching
      ↓
Present / Absent
```

---

## 🛠️ Tech Stack

| Category         | Technologies           |
| ---------------- | ---------------------- |
| Language         | Python                 |
| Frontend         | Streamlit              |
| Computer Vision  | Dlib, Face Recognition |
| Machine Learning | Scikit-learn, SVM      |
| Voice AI         | Resemblyzer            |
| Audio Processing | Librosa                |
| Database         | Supabase / PostgreSQL  |
| Data Processing  | NumPy, Pandas          |
| Security         | Bcrypt                 |

---

## 📂 Project Structure

```text
SnapClass_for_SmartAttendance_using_AI/
│
├── app.py
├── requirements.txt
│
└── src/
    ├── components/
    ├── database/
    ├── pipelines/
    │   ├── face_pipeline.py
    │   └── voice_pipeline.py
    ├── screens/
    └── ui/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sudeb374/SnapClass_for_SmartAttendance_using_AI.git
cd SnapClass_for_SmartAttendance_using_AI
```

### 2. Create environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Supabase

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_KEY"
```

> ⚠️ Never commit API keys or secrets to GitHub.

### 5. Run SnapClass

```bash
streamlit run app.py
```

---

## 🎯 Project Highlights

* 🤖 AI-powered attendance automation
* 👤 Face & voice biometric recognition
* ⚡ Reduces manual attendance effort
* 📊 Centralized attendance management
* 🔐 Secure password handling
* ☁️ Supabase-backed database
* 🖥️ Simple Streamlit interface

---

## 🚀 Future Improvements

* [ ] Real-time webcam attendance
* [ ] Face liveness / anti-spoofing
* [ ] Better speaker diarization
* [ ] Attendance analytics dashboard
* [ ] CSV / Excel / PDF export
* [ ] Email notifications
* [ ] Cloud deployment
* [ ] Advanced role-based access control

---

## 👨‍💻 Author

### Sudeb Kundu

**B.Tech CSE — Artificial Intelligence & Machine Learning**

🔗 GitHub:
https://github.com/sudeb374

---

<p align="center">

⭐ **If you find SnapClass useful, consider giving this repository a star!**

**Built with Python • AI • Computer Vision • Machine Learning • Streamlit**

</p>
