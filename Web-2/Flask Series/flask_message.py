from flask import Flask, request, flash, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "ihatecoding"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")

        if username:
            flash(f"Welcome, {username}")
            flash(f"Wake up boss, {username}")
            return redirect(url_for("index"))
        else:
            flash("Please enter your name")
    return render_template("flash_message.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
