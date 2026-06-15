from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "ihatecoding"
app.config["UPLOAD_FOLDER"] = "uploads/"


@app.route("/upload/single", methods=["GET", "POST"])
def upload_single():
    if request.method == "POST":
        file = request.files["file"]
        if file.filename != "":
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return "File uploaded successfully!"
    return render_template("file_upload.html")


@app.route("/upload/multiple", methods=["GET", "POST"])
def upload_multiple():
    if request.method == "POST":
        print(request.files)
        # for index, file in enumerate(request.files):
        #     print(index, file, enumerate(request.files))
        #     # if file.filename != "":
        #     #     filename = secure_filename(file.filename)
        #     #     file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        #     return "File uploaded successfully!"
    return render_template("file_upload.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
