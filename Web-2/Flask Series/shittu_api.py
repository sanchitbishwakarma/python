from flask import Flask, request, jsonify

app = Flask(__name__)

fake_db = {
    1: {
        "id": 1,
        "name": "Sanchit",
        "resume_text": "Python developer with 1 years experience",
    },
    2: {
        "id": 2,
        "name": "Dev. San",
        "resume_text": "React developer, knows hooks and routing",
    },
}

# data=request.json

# {
#     "resume_text": {{$randomLoremParagraph}},
#     "job_title": {{$randomJobTitle}}
# }


@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.json

    if not data:
        return jsonify({"error": "request body is missing"}), 400

    if "resume_text" not in data:
        return jsonify({"error": "resume_text is missing"}), 400

    if "job_title" not in data:
        return jsonify({"error": "job_title is missing"}), 400

    resume_text = data["resume_text"]
    job_title = data["job_title"]

    mock_score = len(resume_text.split()) * 2

    return (
        jsonify(
            {
                "message": "analysis complete",
                "job_title": job_title,
                "word_count": len(resume_text.split()),
                "match_score": mock_score,
            }
        ),
        200,
    )


@app.route("/api/upload", methods=["POST"])
def upload_resume():
   
    if "resume" not in request.files:
        return jsonify({"error": "file has no name"}), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({"error": "file has no name"}), 400

    content = file.read()
    file_size = len(content)

    return (
        jsonify(
            {
                "message": "file received",
                "content": content.decode(),
                "filename": file.filename,
                "size_bytes": file_size,
            }
        ),
        201,
    )


@app.route("/api/resume/<int:id>", methods=["GET"])
def get_resume(id):
    resume = fake_db.get(id)

    if not resume:
        return jsonify({"error": f"resume with id {id} not found"}), 404

    return jsonify({"data": resume}), 200


if __name__ == "__main__":
    app.run(debug=True)
