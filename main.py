from src.preprocess import load_text, preprocess_text
from src.analysis import get_decomposed_unicode, analyze_text
import nltk
nltk.download('punkt_tab')
import json
import argparse

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

def run_cli(filepath):

    input_text = load_text(filepath)

    tokens = preprocess_text(input_text)
    print(tokens)

    analysis_result = analyze_text(input_text)
    return analysis_result

if __name__ == "__main__":

    filepath = 'data/okm_sample.txt'
    output_data = run_cli(filepath)
    print(output_data)

    output_file = open('data/test.json', 'w', encoding = 'utf-8')
    json.dump(output_data, output_file, ensure_ascii = False, indent = 4, sort_keys = False)
    output_file.close()