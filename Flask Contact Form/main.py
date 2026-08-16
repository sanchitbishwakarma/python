from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    error = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()

        if not name:
            error = "Name required"
        elif not message:
            error = "Message required"
        else:
            return f"Name: {name}, Msg: {message}"
    return render_template("form.html", error=error)


app.run(debug=True)
