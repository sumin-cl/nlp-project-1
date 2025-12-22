from src.preprocess import load_text, preprocess_text
from src.analysis import analyze_features, get_decomposed_unicode, detect_archaic_with_unicode, detect_non_standard_with_unicode#, decompose_syllable_block, detect_archaic_chars
import nltk
nltk.download('punkt_tab')
import langid
import json

def detect_language(input_txt):
    lang, confidence = langid.classify(input_txt)
    return lang, confidence

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

def run_cli():
    input_file = 'data/okm_sample.txt'
    input_text = load_text(input_file)
    tokens = preprocess_text(input_text)
    decomp = get_decomposed_unicode(input_text)
    print(tokens)
    lang_detect = detect_language(input_text)
    print(f'Language: {lang_detect[0]}, Confidence: {lang_detect[1]}')
    features = analyze_features(input_text)
    print(f'Number of Words: {features.get("num_words")}, Number of Sentences: {features.get("num_sentences")}, Average word length: {features.get("avg_word_len")}')
    count = detect_archaic_with_unicode(decomp)
    print(f'Count of Arae-a: {count}')
    non_std = detect_non_standard_with_unicode(decomp)
    print(f'Non-standard characters: {non_std}')
    archaic_hangul = detect_archaic_with_unicode(non_std)
    print(f'Archaic Hangul: {archaic_hangul}')
    #print(f'Count of Arae-a: {count_archaic_chars}')
    output_data = {
        "detection_result": lang_detect,
        "text_statistics": features,
        #"archaic_characters" : count_archaic_chars
        "non_standard": non_std,
        "archaic_hangul": archaic_hangul

    }
    output_file = open('data/test.json', 'w', encoding = 'utf-8')
    json.dump(output_data, output_file, ensure_ascii = False, indent = 4, sort_keys = False)
    output_file.close()

if __name__ == "__main__":
    run_cli()