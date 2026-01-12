from collections import Counter
import src.preprocess as pre

def get_lex_div(text):
    tokens = pre.get_tokens(text)
    tags = pre.get_tags(text)

    total_tokens = len(tokens)
    unique_types = len(set(tokens))

    # Type-Token Ratio (TTR)
    if total_tokens > 0:
        ttr = unique_types / total_tokens
    else:
        ttr = 0.0

    # Hapax Legomena (Einmaliges Vorkommen per Text)
    counts = Counter(tokens)
    hapax_legomena = len([word for word, count in counts.items() if count == 1])

    return {
        "metric": "Lexical Diversity",
        "stats": {
            "total_words": total_tokens,
            "unique_words": unique_types,
            "ttr": round(ttr, 3),
            "hapax_count": hapax_legomena
        }
    }
