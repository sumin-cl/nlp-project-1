from src.preprocess import load_text, preprocess_text
from src.analysis import analyze_text
import nltk
nltk.download('punkt_tab')
import json
import argparse

from src.readability import flesch_simple_check

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

def run_cli(input_filepath, output_filepath, task):
    """Liest von input_filepath, analysiert und schreibt nach output_filepath"""

    input_text = load_text(input_filepath)

    tokens = preprocess_text(input_text)
    print(tokens)
    
    if task == 'korean':

        output_data = analyze_text(input_text)

    elif task == 'readability':
        readability_score = flesch_simple_check(input_text)

        output_data = readability_score

    with open(output_filepath, 'w', encoding='utf-8') as output_file:
        json.dump(output_data, output_file, ensure_ascii = False, indent = 4, sort_keys = False)

    print(f"Analyse erfolgreich. Ergebnis in '{output_filepath} gespeichert.")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Analysiert eine Textdatei auf mittelkoreanische Merkmale')

    parser.add_argument('input_filepath', default='data/okm_sample.txt', help='Pfad zur Input-Textdatei (default: data/okm_sample.txt).')

    parser.add_argument('-o', '--output', default='data/result.json', help='Pfad für die JSON-Datei (default: data/result.json)')
    
    parser.add_argument('--task', choices=['korean', 'readability'], default='korean', help='Choose analysis mode')
    
    args = parser.parse_args()

    run_cli(args.input_filepath, args.output, args.task)