from groq import Groq
import json
import re


def analyze_resume(

    api_key,

    resume_text,

    jd_text

):

    client = Groq(
        api_key=api_key
    )

    prompt = f"""
You are an expert ATS evaluator and recruiter.

Analyze the resume against the job description.

Score using EXACTLY:

Technical Skills Match (0-40)

Projects Relevance (0-20)

Education Match (0-15)

Tools & Technologies Match (0-15)

Domain Alignment (0-10)

ATS Score =
Technical +
Projects +
Education +
Tools +
Domain

Return ONLY JSON.

{{
    "technical_score": 0,
    "projects_score": 0,
    "education_score": 0,
    "tools_score": 0,
    "domain_score": 0,
    "ats_score": 0,

    "job_fit": "",

    "matching_skills": [],

    "missing_skills": [],

    "strengths": [],

    "weaknesses": [],

    "resume_improvements": [],

    "interview_questions": [],

    "executive_summary": ""
}}

Job Fit must be one of:

Poor Fit
Moderate Fit
Strong Fit
Excellent Fit

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.1

    )

    content = (
        response
        .choices[0]
        .message
        .content
    )

    try:
        match = re.search(
            r"\{.*\}",
            content,
            re.DOTALL
        )

        if match:
            print("\n========== GROQ RESPONSE ==========\n")
            print(content)
            print("\n===================================\n")

        return json.loads(
            match.group()
        )

    except Exception as e:
        print("\n========== ERROR ==========\n")
        print(e)

        print("\n========== RAW GROQ RESPONSE ==========\n")
        print(content)

        print("\n=======================================\n")

    return {
        "technical_score": 0,
        "projects_score": 0,
        "education_score": 0,
        "tools_score": 0,
        "domain_score": 0,
        "ats_score": 0,
        "job_fit": "Unknown",
        "matching_skills": [],
        "missing_skills": [],
        "strengths": [],
        "weaknesses": [],
        "resume_improvements": [],
        "interview_questions": [],
        "executive_summary": f"Parse Error:\n{content[:1000]}"
    }