from flask import Flask, request, render_template, jsonify
from src.analysis import analysis_head
import json

app = Flask(__name__)

# Damit Umlaute und Koreanisch im Browser richtig angezeigt werden
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def home():
	return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze_text():
	try:
		input_text = request.form['text_input']
		
		result_dictionary = analysis_head(input_text)

		json_output_string = json.dumps(result_dictionary, indent=4, ensure_ascii=False)

		return render_template('sample_template.html', result=json_output_string)

	except Exception as e:
		return jsonify({"error": str(e)})

if __name__ == '__main__':
	app.run(debug=True)