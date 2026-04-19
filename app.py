from flask import Flask, request, redirect, jsonify
from service import shorten_url, get_url
from flask import render_template

app = Flask(__name__)

@app.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    url = data.get("url")

    try:
        code = shorten_url(url)
        return jsonify({"short_url": f"http://localhost:5000/{code}"})
    except:
        return jsonify({"error": "Invalid URL"}), 400

@app.route("/<code>")
def redirect_url(code):
    url = get_url(code)
    if url:
        return redirect(url)
    return jsonify({"error": "Not found"}), 404

@app.route("/urls")
def list_urls():
    from storage import load_data
    return jsonify(load_data())

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/shorten-ui", methods=["POST"])
def shorten_ui():
    url = request.form.get("url")

    try:
        code = shorten_url(url)
        short_url = f"http://127.0.0.1:5000/{code}"
        return render_template("index.html", short_url=short_url)
    except:
        return render_template("index.html", error="Invalid URL")

if __name__ == "__main__":
    app.run(debug=True)
