from src.preprocess import load_text
from src.analysis import analysis_head
import nltk
nltk.download('punkt_tab')
import langid
import json

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
    
    output_file = open('data/test.json', 'w', encoding = 'utf-8')
    json.dump(output_data, output_file, ensure_ascii = False, indent = 4, sort_keys = False)
    output_file.close()

if __name__ == "__main__":
    run_cli()