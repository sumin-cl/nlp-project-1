from textblob import TextBlob

def sentiment_check(text):
    blob = TextBlob(text)

    # Polarity: -1 (very negative) to +1 (very positive)
    # Subjectivity: 0 (factual) to 1 (opinion)

    pol = blob.sentiment.polarity
    sub = blob.sentiment.subjectivity

    mood = "neutral"
    if pol > 0.1: mood = "positive"
    if pol < 0.1: mood = "negative"

    return {
        "metric": "sentiment analysis",
        "mood": mood,
        "polarity_score": round(pol, 2),
        "subjectivity_score": round(sub, 2)
    }