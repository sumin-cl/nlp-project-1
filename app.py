from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
	return "Hallo, das ist ein Tool zur Analyse von Sprachvarianten mit unterschiedlicher Orthographie"

if __name__ == '__main__':
	app.run(debug=True)