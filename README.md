# 🚀 AI Resume Analyzer Pro

An AI-powered Resume Analyzer that evaluates resumes against job descriptions using **Groq Llama 3**, providing ATS scores, skill-gap analysis, recruiter insights, interview questions, and downloadable PDF reports.
URL :https://ai-resume-analyzer-cxkotgmr5d2ujg59erkt2i.streamlit.app/
---
URL :https://ai-resume-analyzer-cxkotgmr5d2ujg59erkt2i.streamlit.app/

## 🌟 Features

### 📊 ATS Score Analysis

* Evaluates resume compatibility with the job description.
* Provides ATS match percentage.
* Categorizes candidates as:

  * Poor Fit
  * Moderate Fit
  * Strong Fit
  * Excellent Fit

### 🎯 Job Fit Evaluation

* Compares candidate qualifications with role requirements.
* Generates recruiter-style assessments.

### ✅ Skill Matching

* Identifies matching skills between resume and job description.

### ❌ Skill Gap Detection

* Highlights missing skills required for the target role.

### 💪 Strengths Analysis

* Identifies key strengths from the resume.

### ⚠️ Weakness Detection

* Highlights areas that require improvement.

### 🚀 Resume Improvement Suggestions

* Provides actionable recommendations to improve resume quality.

### 🎤 Interview Question Generation

* Generates likely interview questions based on the candidate profile.

### 📄 PDF Report Export

* Downloads a professional PDF report containing all analysis results.

---

# 🛠️ Tech Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Backend Logic             |
| Streamlit  | Web Application           |
| Groq API   | LLM Inference             |
| Llama 3    | AI Analysis               |
| PyPDF      | PDF Text Extraction       |
| ReportLab  | PDF Report Generation     |
| HTML/CSS   | Premium Dashboard Styling |

---

# 🏗️ Project Architecture

```text
Resume PDF
      │
      ▼
PyPDF Text Extraction
      │
      ▼
Resume Text + Job Description
      │
      ▼
Groq Llama 3 Analysis
      │
      ▼
ATS Evaluation Engine
      │
      ▼
Dashboard Visualization
      │
      ▼
PDF Report Export
```

---

# 📂 Project Structure

```text
AI-Resume-Analyzer
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── utils
    ├── ai_analyzer.py
    ├── pdf_reader.py
    └── pdf_report.py
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
```

Move into the project directory:

```bash
cd AI-Resume-Analyzer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 🚀 How To Use

### Step 1

Generate a Groq API Key:

https://console.groq.com

### Step 2

Upload your Resume PDF.

### Step 3

Upload the Job Description PDF.

### Step 4

Click:

```text
Analyze Resume
```

### Step 5

Review:

* ATS Score
* Job Fit
* Matching Skills
* Missing Skills
* Strengths
* Weaknesses
* Resume Improvements
* Interview Questions

### Step 6

Download the PDF Report.

---

# 📊 Output Example

The application generates:

```text
ATS Score: 75%

Job Fit: Strong Fit

Matching Skills:
- Python
- SQL
- Machine Learning

Missing Skills:
- Prompt Engineering
- Customer Success

Strengths:
- Strong technical background
- Research experience

Weaknesses:
- Limited domain exposure
```

---

# 🎯 Interview Explanation

### What problem does this solve?

Recruiters manually compare resumes against job descriptions. This process is time-consuming and inconsistent.

This project automates resume screening using Generative AI and provides recruiter-style feedback instantly.

### How does it work?

1. Extracts text from Resume and Job Description PDFs.
2. Sends both documents to Groq Llama 3.
3. Performs ATS analysis and skill matching.
4. Generates recruiter insights.
5. Creates a downloadable PDF report.

### Why Groq?

Groq provides extremely fast inference for large language models, enabling real-time resume analysis.

---

# 🔮 Future Improvements

* Multi-resume comparison
* Resume ranking system
* Cover letter generation
* Resume rewriting assistant
* Job recommendation engine
* LinkedIn profile analysis

---

# 👨‍💻 Author

### Ayush Sankhyan

BE CSE (Hons.) Artificial Intelligence & Machine Learning

Chandigarh University

---

## ⭐ If you found this project useful, consider giving it a star!
