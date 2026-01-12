import textstat

def flesch_simple_check(txt):
    # Flesch Reading Ease Metrik
    score = textstat.flesch_reading_ease(txt)

    print (f"Flesch Score: {score}")

    level = "Standard"
    if score > 90: level = "Very Easy"
    if score < 90: level = "Easy"
    if score < 70: level = "Standard"
    if score < 50: level = "Difficult"
    elif score < 30: level = "Confusing"

    return {"metric": "readability score", "score": score, "level": level}
