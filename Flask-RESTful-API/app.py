from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        req = request.get_json()
        print(req)
        return jsonify(req) 

    data = {
        "name": "Sanchit",
        "skill": ["devops", "aws", "love"],
        "bio": "mistakenly became programmer",
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
