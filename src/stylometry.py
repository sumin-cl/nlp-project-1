import nltk
from collections import Counter
import src.preprocess as pre

def get_adjectives(text):
    tag_set = pre.get_tags(text)
    
    adjectives = [word.lower() for word, tag in tag_set if tag.startswith('JJ')]
    counts = Counter(adjectives).most_common(5)

    return {
        "metric": "stylometry (adjectives)",
        "total_adj": len(adjectives),
        "top_5": dict(counts)
    }
    