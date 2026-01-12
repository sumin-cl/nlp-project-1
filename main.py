from src.preprocess import load_text, get_tokens
from src.analysis import analyze_text
import nltk
import json
import argparse
import os

from src.sentiment import sentiment_check
from src.readability import flesch_simple_check
from src.stylometry import get_style_stats
from src.diversity import get_lex_div

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

def run_cli(input_filepath, task):
    """Liest von input_filepath, analysiert und schreibt nach output_filepath"""

    input_text = load_text(input_filepath)

    tokens = get_tokens(input_text)

    final_report = {
        "meta": {
            "text_length": len(input_text),
            "task_requested": task
        },
        "analysis": {}
    }

    def add_result(key, data):
        final_report["analysis"][key] = data
    
    if task == "all":
        print("...Full analysis...")
        add_result("readability", flesch_simple_check(input_text))
        add_result("sentiment", sentiment_check(input_text))
        add_result("stylometry", get_style_stats(input_text))
        add_result("diversity", get_lex_div(input_text))

    elif task == 'readability':
        readability_score = flesch_simple_check(input_text)
        add_result("readability", readability_score)

    elif task == 'sentiment':
        sentiment_scores = sentiment_check(input_text)
        add_result("sentiment", sentiment_scores)

    elif task == 'stylometry':
        stylometry = get_style_stats(input_text)
        add_result("stylometry", stylometry)

    elif task == "diversity":
        lex_div = get_lex_div(input_text)
        add_result("diversity", lex_div)

    elif task == 'orthography':
        orth_output = analyze_text(input_text)
        add_result("orthography", orth_output)

    return final_report

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Analysiert eine Textdatei auf mittelkoreanische Merkmale')

    parser.add_argument('input_filepath', default='data/input/test.txt', help='Pfad zur Input-Textdatei (default: data/test.txt).')

    parser.add_argument('-o', '--output', default='data/output/result.json', help='Pfad für die JSON-Datei (default: data/result.json)')
    
    parser.add_argument('--task', choices=['all', 'readability', 'sentiment', 'stylometry', 'diversity', 'orthography'], default='all', help='Choose analysis mode')
    
    args = parser.parse_args()

    output_data = run_cli(args.input_filepath, args.task)

    if args.output:

        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=4, sort_keys=False, ensure_ascii=False)
            print("Gespeichert als JSON")

    else:
        print(json.dumps(output_data, indent=4, ensure_ascii=False))