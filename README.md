# Spracherkenner
Dieses Mini-Projekt soll erkennen in welcher Sprache ein Text geschrieben ist.

Es unterscheidet modernes und historisches Koreanisch.

Methode: Zerlegung in Jamo (NFD) und Abgleich mit einer Liste moderner Standard-Zeichen.

Erkennt auch Hanja und Arae-a.

Input via Textdatei, Output via JSON.

* Tools: Python 3.9

* Externe Libraries: NLTK, langid

## Setup

### Schritte zur Einrichtung der Virtual Environment (venv), um die Abhängigkeiten (packages) zu installieren:

1. Erstellung der venv mit: `python -n venv venv`
2. Aktivierung: `.\venv\Scripts\Activate.ps1` (Windows) oder `source venv/bin/activate` (Linux/Mac)
3. Installation der erforderlichen Pakete: `pip install -r requirements.txt`

## Beispieloutput

![CLI output](example_output_cli.png)

## JSON

<img
src="example_output_json.png"
alt="JSON Output" width="500">