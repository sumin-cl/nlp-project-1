import nltk
import unicodedata
from jamo import h2j, j2hcj

def analyze_features(text):
    word_list = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)

    num_words = len(word_list)

    avg_word_len = sum(len(w) for w in word_list) / num_words if num_words > 0 else 0

    return {
        "num_words": num_words,
        "num_sentences": len(sentences),
        "avg_word_len": avg_word_len
    }

def decompose_syllable_block(text):  # External library
    decomposed = h2j(text)

    compat_jamo = j2hcj(decomposed)

    return compat_jamo

def decompose_unicode(text):
    decomposed = unicodedata.normalize('NFD', text)
    
    return decomposed

def detect_archaic_chars(text):
    arae_a_char = 'ㆍ'

    decomposed_text = decompose_syllable_block(text)
    #print(type(decomposed_text))
    #print(decomposed_text)
    
    count = decomposed_text.count(arae_a_char)

    return count

def detect_with_unicode(text):

    decomposed_unicode = decompose_unicode(text)
    #print(decomposed_unicode)
    for ch in decomposed_unicode:
        if "ARAEA" in unicodedata.name(ch):
            print(ch, unicodedata.name(ch))