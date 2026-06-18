import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.ai_analyzer import analyze_resume
from utils.pdf_report import generate_pdf_report

# --------------------------------------------------

# PAGE CONFIG

# --------------------------------------------------

st.set_page_config(
page_title="AI Resume Analyzer Pro",
page_icon="🚀",
layout="wide"
)

# --------------------------------------------------

# CUSTOM CSS

# --------------------------------------------------

st.markdown("""

<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0F172A,
        #111827
    );
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

.block-container {
    padding-top: 1.5rem;
    max-width: 1200px;
}

div[data-testid="metric-container"] {
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 18px;
    padding: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
}

.skill-green {
    background:#064E3B;
    color:#A7F3D0;
    padding:8px 14px;
    border-radius:20px;
    display:inline-block;
    margin:4px;
    font-weight:600;
}

.skill-red {
    background:#7F1D1D;
    color:#FECACA;
    padding:8px 14px;
    border-radius:20px;
    display:inline-block;
    margin:4px;
    font-weight:600;
}

.summary-card {
    background:#1E293B;
    border:1px solid #334155;
    padding:20px;
    border-radius:18px;
}

</style>

""", unsafe_allow_html=True)

# --------------------------------------------------

# HEADER

# --------------------------------------------------

st.title("🚀 AI Resume Analyzer Pro")

st.caption(
"ATS Evaluation • Skill Gap Analysis • Recruiter Insights"
)

# --------------------------------------------------

# SIDEBAR

# --------------------------------------------------

st.sidebar.title("⚡ Settings")

api_key = st.sidebar.text_input(
"Groq API Key",
type="password"
)

st.sidebar.markdown("---")

st.sidebar.markdown("""

### 🔑 Get Free Groq API Key

1. Visit:
   https://console.groq.com

2. Create Account

3. Generate API Key

4. Paste it above

---

### Features

✅ ATS Score

✅ Job Fit Analysis

✅ Skill Gap Detection

✅ Recruiter Insights

✅ Resume Improvements

✅ Interview Questions

✅ PDF Report Export

---

🔒 API keys are never stored.
""")

# --------------------------------------------------

# FILE UPLOADS

# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

with col2:
    jd_file = st.file_uploader(
    "📋 Upload Job Description",
    type=["pdf"]
)

# --------------------------------------------------

# ANALYSIS

# --------------------------------------------------

if resume_file and jd_file:

    if not api_key:

        st.warning(
            "Please enter your Groq API Key."
        )

    else:

        if st.button(
            "🚀 Analyze Resume",
            use_container_width=True
        ):

            with st.spinner(
                "Analyzing Resume..."
            ):

                resume_text = extract_text_from_pdf(
                    resume_file
                )

                jd_text = extract_text_from_pdf(
                    jd_file
                )

                result = analyze_resume(
                    api_key,
                    resume_text,
                    jd_text
                )

            ats_score = result.get(
                "ats_score",
                0
            )

            job_fit = result.get(
                "job_fit",
                "Unknown"
            )

            matching_skills = result.get(
                "matching_skills",
                []
            )

            missing_skills = result.get(
                "missing_skills",
                []
            )

            strengths = result.get(
                "strengths",
                []
            )

            weaknesses = result.get(
                "weaknesses",
                []
            )

            improvements = result.get(
                "resume_improvements",
                []
            )

            interview_questions = result.get(
                "interview_questions",
                []
            )

            summary = result.get(
                "executive_summary",
                ""
            )

            # TOP METRICS

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                 st.metric(
                     "ATS Score",
                     f"{ats_score}%"
                )
            with c2:
                st.metric(
                    "Job Fit",
                    job_fit
                )

            with c3:
                st.metric(
                    "Matched Skills",
                    len(matching_skills)
                )

            with c4:
                st.metric(
                    "Missing Skills",
                    len(missing_skills)
                )

            # ATS BAR

            st.markdown("### ATS Match")

            st.progress(
                min(
                    ats_score / 100,
                    1.0
                )
            )

            if ats_score >= 70:
                st.success("🟢 Strong ATS Match")
            elif ats_score >= 50:
                st.warning("🟠 Moderate ATS Match")
            else:
                st.error("🔴 Needs Improvement")

            # JOB FIT

            if job_fit == "Poor Fit":
                st.error("🔴 Poor Fit")
            elif job_fit == "Moderate Fit":
                st.warning("🟠 Moderate Fit")
            elif job_fit == "Strong Fit":
                st.success("🟢 Strong Fit")
            else:
                st.info("⭐ Excellent Fit")

            # SUMMARY

            st.markdown("## 📋 Executive Summary")

            st.markdown(
                f"""
                <div class="summary-card">
                {summary}
                </div>
                """,
                unsafe_allow_html=True
            )

            # SKILLS

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("## ✅ Matching Skills")

                for skill in matching_skills:
                    st.markdown(
                        f'<span class="skill-green">{skill}</span>',
                        unsafe_allow_html=True
                    )

            with col2:

                st.markdown("## ❌ Missing Skills")

                for skill in missing_skills:
                    st.markdown(
                        f'<span class="skill-red">{skill}</span>',
                        unsafe_allow_html=True
                    )

            # DETAILS

            with st.expander("💪 Strengths"):
                for item in strengths:
                    st.success(item)

            with st.expander("⚠️ Weaknesses"):
                for item in weaknesses:
                    st.warning(item)

            with st.expander("🚀 Resume Improvements"):
                for item in improvements:
                    st.info(item)

            with st.expander("🎯 Interview Questions"):
                for i, question in enumerate(
                    interview_questions,
                    start=1
                ):
                    st.write(f"{i}. {question}")

            # PDF REPORT

            pdf_path = "resume_report.pdf"

            generate_pdf_report(
                pdf_path,
                ats_score,
                job_fit,
                summary,
                matching_skills,
                missing_skills,
                strengths,
                weaknesses,
                improvements,
                interview_questions
            )

            with open(
                pdf_path,
                "rb"
            ) as pdf_file:

                st.download_button(
                    "📄 Download Professional PDF Report",
                    pdf_file,
                    file_name="AI_Resume_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

# --------------------------------------------------

# FOOTER

# --------------------------------------------------

st.markdown("---")

st.markdown(
""" <div style='text-align:center;color:#94A3B8'>
Powered by Groq • Streamlit • AI Resume Analysis<br>
Built with ❤️ by <b>Ayush Sankhyan</b> </div>
""",
unsafe_allow_html=True
)
