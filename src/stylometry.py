import nltk
from collections import Counter
import src.preprocess as pre

def _filter_by_tag(tags, prefix):
    """Filters words based off tag-prefix (JJ, NN, VB,...)."""
    return [word.lower() for word, tag in tags if tag.startswith(prefix) and word.isalpha()]

def _get_stats(word_list):
    """Counts 5 most common words"""
    return {
        "count": len(word_list),
        "top_5": dict(Counter(word_list).most_common(5))
    }

def get_style_stats(text):
    tags = pre.get_tags(text)

    adjs = _filter_by_tag(tags, 'JJ')
    nouns = _filter_by_tag(tags, 'NN')
    verbs = _filter_by_tag(tags, 'VB')
    advs = _filter_by_tag(tags, 'RB')

    return {
        "metric": "Stylometry (POS Distribution)",
        "details": {
            "adjectives": _get_stats(adjs),
            "nouns": _get_stats(nouns),
            "verbs": _get_stats(verbs),
            "adverbs": _get_stats(advs)
        }
    }