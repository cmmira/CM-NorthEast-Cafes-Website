from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

cafes = requests.get("http://127.0.0.1:5000/all").json()

@app.route("/")
def home():
    return render_template("index.html", cafes=cafes['cafes'])

if __name__ == "__main__":
    app.run(debug=True, port=5001)