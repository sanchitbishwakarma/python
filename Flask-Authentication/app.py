from flask import Flask, session, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.secret_key = "sanchitisthekey"  # choose your own key, this is mine

database = {"username": "sanchit", "password": "sanchit123", "name": "Syntax Render"}


# login route and controller logic
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if not (username and password):
            flash("Username and password required", category="error")
            return redirect(url_for("login"))

        if not (username == database["username"] and password == database["password"]):
            flash("Invalid credentials", category="error")
            return redirect(url_for("login"))

        session["user"] = database["name"]
        return redirect(url_for("dashboard_page"))

    return render_template("login_page.html")


# dashboard page after login only
@app.route("/dashboard", methods=["GET"])
def dashboard_page():
    user = session.get("user", None)
    if user == None:
        return redirect(url_for("login"))

    return render_template("dashboard_page.html", user=user)


# logout user
@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
