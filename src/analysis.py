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

# Also include conjoining jamo (choseong/jungseong) ranges so decomposed
# syllables (NFD) and compatibility jamo compare correctly.
CHOSEONG = [chr(cp) for cp in range(0x1100, 0x1113)]  # 19 initial consonants
JUNGSEONG = [chr(cp) for cp in range(0x1161, 0x1176)]  # 21 medial vowels

HANGUL_UNICODE_NAMES = set({unicodedata.name(char, "UNNAMED") for char in (HANGUL_CHARACTERS | set(CHOSEONG) | set(JUNGSEONG))})

# Archaic Hangul characters
ARCHAIC_CHOSEONG = [chr(cp) for cp in range(0x1114, 0x115F)]
ARCHAIC_JUNGSEONG = [chr(cp) for cp in range(0x1177, 0x11A2)]

ARCHAIC_HANGUL_UNICODE_NAMES = set({unicodedata.name(char, "UNNAMED") for char in (HANGUL_CHARACTERS | set(ARCHAIC_CHOSEONG) | set(ARCHAIC_JUNGSEONG))})

arae_a_char = 'ㆍ'

### Preprocessing ###
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

### Syllable block decomposition & character detection ###
def get_decomposed_unicode(text):  # Unicode implement
    decomposed = unicodedata.normalize('NFD', text)
    
    return decomposed

def detect_non_standard_with_unicode(decomposed):
    '''Compare the unicodedata names of conjoining jamo used in unicodedata'''
    non_standard_counts = {}

    decomposed_names = [unicodedata.name(char, "UNNAMED") for char in decomposed]

    for ch in decomposed_names:
        if ch not in HANGUL_UNICODE_NAMES:
            non_standard_counts[ch] = non_standard_counts.get(ch, 0) + 1
    return non_standard_counts

def detect_archaic_with_unicode(non_standard_counts):
    archaic_hangul = {}

    for ch in non_standard_counts:
        if ch in ARCHAIC_HANGUL_UNICODE_NAMES:
            archaic_hangul[ch] = archaic_hangul.get(ch, non_standard_counts[ch])
    
    return archaic_hangul