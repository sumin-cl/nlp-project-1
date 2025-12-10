import nltk
nltk.download('punkt_tab')
import langid
import json

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
def preprocess_text(input_txt):
    text_lower = input_txt.lower()
    tokens = nltk.word_tokenize(text_lower)
    return tokens
def detect_language(input_txt):
    lang, confidence = langid.classify(input_txt)
    return lang, confidence

if __name__ == "__main__":
    input_file = 'test.txt'
    input_text = load_text(input_file)
    tokens = preprocess_text(input_text)
    print(tokens)
    lang_detect = detect_language(input_text)
    print(f"Language: {lang_detect[0]}, Confidence: {lang_detect[1]}")
    output_file = open("test.json", "w")
    json.dump(lang_detect, output_file, indent = 4, sort_keys = False)
    output_file.close