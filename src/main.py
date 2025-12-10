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
def dict_to_json(input, indent=4, sort_keys=False):
    """
    Convert a Python dictionary to a JSON-formatted string.
    
    :param input: Dictionary to convert
    :param indent: Indentation level for pretty-printing (default: 4)
    :param sort_keys: Whether to sort keys alphabetically (default: False)
    :return: JSON string
    """
    json_str = json.dumps(input, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
    return json_str

if __name__ == "__main__":
    input_file = 'test.txt'
    input_text = load_text(input_file)
    tokens = preprocess_text(input_text)
    print(tokens)
    lang_detect = detect_language(input_text)
    print(f'Language: {lang_detect[0]}, Confidence: {lang_detect[1]}')
    features = analyze_features(input_text)
    print(f'Number of Words: {features.get("num_words")}, Number of Sentences: {features.get("num_sentences")}, Average word length: {features.get("avg_word_len")}')
    output_data = {
        "detection_result": lang_detect,
        "text_statistics": features
    }
    output_file = open("test.json", "w")
    json.dump(output_data, output_file, indent = 4, sort_keys = False)
    output_file.close()