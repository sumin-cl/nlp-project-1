import math
from collections import Counter

def calculate_entropy(text_tokens):
    """Berechnet die Shannon-Entropie einer Token-Liste."""
    if not text_tokens:
        return 0.0
    # 1. Häufigkeiten zählen
    counts = Counter(text_tokens)
    total_count = len(text_tokens)

    entropy = 0.0

    # 2. Wahrscheinlichkeiten und Summe berechnen
    for word in counts:
        p = counts[word] / total_count
        entropy -= p * math.log2(p) #  Shannon-Formel
    
    return entropy