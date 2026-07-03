def generate_suggestions(resume_text, skills, ats_score):

    suggestions = []

    if ats_score < 70:
        suggestions.append("Improve your resume structure to increase ATS score.")

    if "github" not in resume_text.lower():
        suggestions.append("Add your GitHub profile link.")

    if "linkedin" not in resume_text.lower():
        suggestions.append("Add your LinkedIn profile.")

    if "certification" not in resume_text.lower():
        suggestions.append("Add relevant certifications.")

    if len(skills) < 5:
        suggestions.append("Include more technical skills.")

    if len(resume_text.split()) < 300:
        suggestions.append("Expand your resume with projects and achievements.")

    if "project" not in resume_text.lower():
        suggestions.append("Include at least one technical project.")

    if not suggestions:
        suggestions.append("Excellent resume! Very few improvements needed.")

    return suggestions