# 🤖 TalentScout Hiring Assistant

An intelligent Hiring Assistant chatbot built for **initial technical screening** of candidates at *TalentScout*, a fictional recruitment agency specializing in technology placements.
The chatbot leverages **Large Language Models (LLMs)** and **prompt engineering** to collect candidate information, generate experience-aware technical questions, and assist recruiters with structured interview insights.

---

## 🎯 Project Objective

The main goal of this project is to demonstrate:

* Effective **prompt engineering**
* Context-aware conversational flow
* Dynamic technical question generation based on **tech stack and experience**
* Practical usage of **LLMs in real-world hiring workflows**

This bot acts as a **Junior Hiring Assistant**, handling initial screening before human recruiters take over.

---

## 🚀 Key Features

### 🧾 Candidate Information Collection

* Full Name
* Email Address (validated)
* Phone Number (validated)
* Years of Experience
* Desired Role
* Current Location
* Tech Stack

### ✏️ Error Handling & Editing

* Input validation for email, phone, and experience
* Candidates can **edit incorrect details** before proceeding
* Confirmation step before interview begins

### 🧠 Intelligent Interviewing

* Generates **3–5 technical questions**
* Questions adapt to:

  * Candidate’s **tech stack**
  * Candidate’s **experience level**
* Asks questions **one by one**
* Provides **brief AI-based assessment** for each answer

### 📄 Interview Review Support

* Stores structured interview data (Q&A + assessments)
* Can be exported as a file for **senior recruiters / hiring managers**
* Enables **asynchronous review** of interviews

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Frontend/UI:** Streamlit
* **LLM Provider:** Groq (LLaMA 3.3 – 70B)
* **Environment Management:** python-dotenv
* **Prompt Engineering:** Custom system & user prompts

---

## 🧩 Architecture Overview

```
Candidate
   ↓
Streamlit UI
   ↓
Junior Hiring Assistant (LLM)
   ↓
Structured Interview Data
   ↓
Downloadable Report
   ↓
Senior Recruiter Review
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/TalentScout-Hiring-Assistant.git
cd TalentScout-Hiring-Assistant
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

> ⚠️ `.env` is ignored using `.gitignore` to protect sensitive keys.

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The app will open in your browser and guide the candidate through the hiring flow.

---

## 🧠 Prompt Engineering Strategy

* Separate **system** and **user** prompts
* Explicit constraints to control:

  * Question relevance
  * Difficulty level
  * Output format
* Experience-aware prompts ensure **fair assessment** for junior, mid, and senior candidates

---

## 🔐 Data Privacy & Security

* Uses **simulated data**
* No permanent storage of candidate information
* API keys managed via environment variables
* Designed with **GDPR-friendly principles**

---

## 🧪 Limitations & Future Enhancements

* Resume parsing and auto-fill
* PDF report generation
* Recruiter dashboard
* Candidate scoring & ranking
* Cloud deployment (i'm doing in Render )

---

## 📌 Conclusion

This project demonstrates how **LLMs can be applied responsibly and effectively** in recruitment workflows, automating repetitive screening tasks while keeping humans in the loop for final decisions.

