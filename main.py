from src.preprocess import load_text, get_tokens
from src.analysis import analyze_text
import nltk
import json
import argparse
import os

from rich.console import Console
from rich.table import Table
from rich import print as rprint

from src.sentiment import sentiment_check
from src.readability import flesch_simple_check
from src.stylometry import get_style_stats
from src.diversity import get_lex_div
from src.entropy import calculate_entropy

from src.visualization import plot_pos_stats

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
        add_result("entropy", calculate_entropy(tokens))

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

def print_report(data):
    console = Console()

    console.print("\n[bold green] NLP analysis[/bold green]", justify = "center")
    console.print(f"Task: [cyan]{data['meta']['task_requested']}[/cyan] | Length: [cyan]{data['meta']['text_length']} chars[/cyan]")
    
    analysis = data.get("analysis", {})
    if "readability" in analysis:
        read_score = analysis['readability']
        table = Table(title="Readability/Complexity Analysis")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_column("Verdict", style="green")

        table.add_row("Flesch Score", str(round(read_score['score'], 1)), read_score['level'])

        console.print(table)
        console.print("")

    if "sentiment" in analysis:
        sent = analysis['sentiment']
        table = Table(title="Sentiment Analysis")
        table.add_column("Metric", style="cyan")
        table.add_column("Score", style="magenta")
        table.add_column("Mood", style="green")

        table.add_row("Polarity", str(sent['polarity_score']), sent['mood'])
        table.add_row("Subjectivity", str(sent['subjectivity_score']), "0=Fact, 1=Opinion")

        console.print(table)
        console.print("")

    if "stylometry" in analysis:
        style_metric = analysis['stylometry']['details']
        table = Table(title="Stylometry Analysis")
        table.add_column("Category", style="cyan")
        table.add_column("Count", style="magenta")
        table.add_column("Top Words", style="yellow")

        for cat, details in style_metric.items():
            top_words = ", ".join(details["top_5"].keys())
            table.add_row(cat.capitalize(), str(details["count"]), top_words)

        console.print(table)
        console.print("")

    if "diversity" in analysis:
        div = analysis['diversity']['stats']
        table = Table(title="Lexical Diversity")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        
        table.add_row("Unique Words", str(div["unique_words"]))
        table.add_row("TTR (Variety)", str(div["ttr"]))
        table.add_row("Unique Once (Hapax)", str(div["hapax_count"]))
        
        console.print(table)
        console.print("")

    if "entropy" in analysis:
        entropy = analysis['entropy']

        console.print("Shannon-Entropy: ", entropy)  
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Untersucht einen Text auf verschiedene NLP Metriken')

    parser.add_argument('input_filepath', default='data/input/test.txt', help='Pfad zur Input-Textdatei (default: data/test.txt).')

    parser.add_argument('-o', '--output', default='data/output/result.json', help='Pfad für die JSON-Datei (default: data/result.json)')
    
    parser.add_argument('--task', choices=['all', 'readability', 'sentiment', 'stylometry', 'diversity', 'orthography'], default='all', help='Choose analysis mode')
    
    args = parser.parse_args()

    output_data = run_cli(args.input_filepath, args.task)

    print_report(output_data)

    if args.output:

        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=4, sort_keys=False, ensure_ascii=False)
            print("Gespeichert als JSON")

    else:
        print(json.dumps(output_data, indent=4, ensure_ascii=False))

    base_name = os.path.basename(args.input_filepath)

    if base_name.endswith(".txt"):
        base_name = base_name[:-4]

    if "stylometry" in output_data.get("analysis", {}):
        plot_dir = os.path.join("data", "plots")
        img_path = os.path.join(plot_dir, f"plot_{base_name}.png")
        
        style_stats = output_data["analysis"]["stylometry"]["details"]
        plot_pos_stats(style_stats, img_path)
        print(f"🎨 Plot gespeichert: {img_path}")