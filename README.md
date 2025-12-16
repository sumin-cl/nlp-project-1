# Spracherkenner
Dieses Mini-Projekt soll erkennen in welcher Sprache ein Text geschrieben ist.

Es unterscheidet modernes und historisches Koreanisch.

Methode: Zerlegung in Jamo (NFD) und Abgleich mit einer Liste moderner Standard-Zeichen

Erkennt auch Hanja und Arae-a

Input via Textdatei, Output via JSON.

* Tools: Python 3.9

* Libraries: NLTK, langid

## Setup

### Schritte zur Einrichtung der Virtual Environment (venv), um die Abhängigkeiten (packages) zu installieren:

1. Erstelle die venv: `python -n venv venv`
2. Aktiviere sie: `.\venv\Scripts\Activate.ps1` (Windows) oder `source venv/bin/activate` (Linux/Mac)
3. Installiere die Pakete: `pip install -r requirements.txt`
