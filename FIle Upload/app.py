from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return """
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>

    <img id="preview" width="300">

<script>
document.querySelector('input[type="file"]').onchange = function () {
    document.getElementById('preview').src = URL.createObjectURL(this.files[0]);
};
</script>
    """


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    return f"File saved successfully: {file.filename}"


if __name__ == "__main__":
    app.run(debug=True)
