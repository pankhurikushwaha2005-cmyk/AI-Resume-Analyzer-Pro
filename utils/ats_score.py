import re

def calculate_ats_score(text):

    score = 0

    word_count = len(text.split())

    if word_count > 300:
        score += 20

    if re.search(r"education", text.lower()):
        score += 20

    if re.search(r"skills", text.lower()):
        score += 20

    if re.search(r"experience", text.lower()):
        score += 20

    if re.search(r"project", text.lower()):
        score += 20

    return min(score, 100)