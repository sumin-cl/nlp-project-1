from flask import Flask, request, jsonify
from src.analysis import analyze_features, get_decomposed_unicode, detect_non_standard_with_unicode, detect_archaic_with_unicode

app = Flask(__name__)

# Damit Umlaute und Koreanisch im Browser richtig angezeigt werden
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def home():
	return "<h1>Mittelkoreanisch Analyse API<h1/><p>Benutze:/analyze?text=DeinText</p>"

@app.route('/analyze')
def analyze_text():
	input_text = request.args.get('text', '')

	if not input_text:
		return jsonify({"error": "Kein Text gefunden. Bitte ?text=... an die URL anhängen"})
	
	try:
		result = analyze_features(input_text)

		decomp = get_decomposed_unicode(input_text)
		non_std = detect_non_standard_with_unicode(decomp)
		archaic_hangul = detect_archaic_with_unicode(non_std)

		return jsonify(result, non_std, archaic_hangul)
	
	except Exception as e:
		return jsonify({"error": str(e)})


if __name__ == '__main__':
	app.run(debug=True)