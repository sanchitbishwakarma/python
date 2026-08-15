from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "test_secret_key"


@app.route("/")
def hellow():
    return "Hello Boss"


@app.route("/html")
def htmlFrom():
    return render_template("htmlFrom.html")


@app.route("/hotel")
def greetHotel():
    name = request.args.get("name", "Guest")
    return f"Hello {name}"


@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "POST":
        msg = request.form.get("message")
        if not msg:
            flash("Error: Message cannot be empty!")
        else:
            flash(f"Success: Message received: {msg}")
        return redirect(url_for("message"))
    return render_template("htmlFrom.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001, host="127.0.0.1")
