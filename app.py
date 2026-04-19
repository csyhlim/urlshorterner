from flask import Flask, request, redirect, jsonify
from service import shorten_url, get_url

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

if __name__ == "__main__":
    app.run(debug=True)