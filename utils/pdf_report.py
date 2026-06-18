from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf_report(
    file_path,
    ats_score,
    job_fit,
    summary,
    matching_skills,
    missing_skills,
    strengths,
    weaknesses,
    improvements,
    interview_questions
):
    doc = SimpleDocTemplate(
        file_path
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AI Resume Analyzer Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            f"<b>ATS Score:</b> {ats_score}%",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Job Fit:</b> {job_fit}",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            "Executive Summary",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    sections = [
        ("Matching Skills", matching_skills),
        ("Missing Skills", missing_skills),
        ("Strengths", strengths),
        ("Weaknesses", weaknesses),
        ("Resume Improvements", improvements),
        ("Interview Questions", interview_questions)
    ]

    for title, items in sections:
        elements.append(
            Paragraph(
                title,
                styles["Heading2"]
            )
        )

        for item in items:
            elements.append(
                Paragraph(
                    f"• {item}",
                    styles["BodyText"]
                )
            )

        elements.append(
            Spacer(1, 8)
        )

    doc.build(
        elements
    )
