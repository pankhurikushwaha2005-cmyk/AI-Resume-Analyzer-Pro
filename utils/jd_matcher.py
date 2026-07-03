from utils.skill_extractor import extract_skills

def match_resume_with_jd(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    matching_skills = list(set(resume_skills) & set(jd_skills))
    missing_skills = list(set(jd_skills) - set(resume_skills))

    if len(jd_skills) == 0:
        match_percentage = 0
    else:
        match_percentage = int(
            (len(matching_skills) / len(jd_skills)) * 100
        )

    return (
        match_percentage,
        matching_skills,
        missing_skills
    )