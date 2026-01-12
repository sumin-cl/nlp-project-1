import matplotlib.pyplot as plt
import os

def plot_pos_stats(style_data, save_path):
    """Erstellt ein Balkendiagramm für die POS-Verteilung"""
    categories = list(style_data.keys())
    counts = [style_data[cat]['count'] for cat in categories]

    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

    plt.figure(figsize=(8, 6))
    bars = plt.bar(categories, counts, color=colors)

    plt.title('Stylometry Analysis: Part-of-Speech Distribution', fontsize=14)
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}', ha='center', va='bottom')

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    plt.savefig(save_path)
    plt.close()

    return save_path
