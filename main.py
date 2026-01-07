from src.preprocess import load_text, get_tokens
from src.analysis import analyze_text
import nltk
import json
import argparse

from src.sentiment import sentiment_check
from src.readability import flesch_simple_check
from src.stylometry import get_adjectives

try:
    nltk.data.find('punkt_tab')
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('taggers/averaged_perceptron_tagger_eng')

except LookupError:
    nltk.download('punkt_tab')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger_eng')

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

    tokens = get_tokens(input_text)
    #print(tokens)
    
    if task == 'korean':

        output_data = analyze_text(input_text)

    elif task == 'readability':
        readability_score = flesch_simple_check(input_text)

        output_data = readability_score

    elif task == 'sentiment':
        sentiment_scores = sentiment_check(input_text)

        stylometry_adj = get_adjectives(input_text)

        output_data = sentiment_scores, stylometry_adj

    with open(output_filepath, 'w', encoding='utf-8') as output_file:
        json.dump(output_data, output_file, ensure_ascii = False, indent = 4, sort_keys = False)

    print(f"Analyse erfolgreich. Ergebnis in '{output_filepath} gespeichert.")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Analysiert eine Textdatei auf mittelkoreanische Merkmale')

    parser.add_argument('input_filepath', default='data/input/okm_sample.txt', help='Pfad zur Input-Textdatei (default: data/okm_sample.txt).')

    parser.add_argument('-o', '--output', default='data/output/result.json', help='Pfad für die JSON-Datei (default: data/result.json)')
    
    parser.add_argument('--task', choices=['korean', 'readability', 'sentiment'], default='korean', help='Choose analysis mode')
    
    args = parser.parse_args()

    run_cli(args.input_filepath, args.output, args.task)