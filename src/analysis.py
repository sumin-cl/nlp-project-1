import nltk
import unicodedata
# from jamo import h2j, j2hcj

# Consonants (자음) - 19 characters
HANGUL_CONSONANTS = {
    'ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅉ', 
    'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㄲ', 'ㄸ', 'ㅃ', 'ㅆ'
}

# Vowels (모음) - 21 characters
HANGUL_VOWELS = {
    'ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ',
    'ㅐ', 'ㅒ', 'ㅔ', 'ㅖ', 'ㅘ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ'
}

# All Hangul characters (40 total)
HANGUL_CHARACTERS = HANGUL_CONSONANTS | HANGUL_VOWELS

HANGUL_UNICODE_NAMES = {unicodedata.name(char, "UNNAMED") for char in HANGUL_CHARACTERS}

arae_a_char = 'ㆍ'

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

'''
def get_decomposed_syllable_block(text):  # External library
    decomposed = h2j(text)

    compat_jamo = j2hcj(decomposed)

    return compat_jamo

def detect_archaic_chars(text):

    decomposed_text = get_decomposed_syllable_block(text)
    
    count = decomposed_text.count(arae_a_char)

    return count
'''

def get_decomposed_unicode(text):  # Unicode implement
    decomposed = unicodedata.normalize('NFD', text)
    
    return decomposed

def detect_archaic_with_unicode(decomposed):
    count = 0

    #print(decomposed_unicode)
    for ch in decomposed:
        if "HANGUL JUNGSEONG ARAEA" in unicodedata.name(ch):
            count += 1
    
    return count

def detect_non_standard_with_unicode(decomposed):

    non_standard_counts = {}
    #print(decomposed_unicode)
    for ch in decomposed:
        if ch not in HANGUL_CHARACTERS:
            non_standard_counts[ch] = non_standard_counts.get(ch, 0) + 1
    return non_standard_counts