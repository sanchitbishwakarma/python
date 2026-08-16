from flask import Flask, session, request, redirect, url_for, flash, render_template

app = Flask(__name__)
app.secret_key = "love"  # this is my secret key, find your own


# root home page
@app.route("/", methods=["GET"])
def home_page():
    user = session.get("user", "Guest")

    if user != "Guest":
        return (
            f"Welcome {user['name']}"
            f"Your email: {user['email']}"
            f"age: {user['age']}"
        )
    return (
        f"Welcome {user}<br>"
        f"Register here: <a href='{url_for('registration_form')}'>click me</a>"
    )


# registration form
@app.route("/register", methods=["GET", "POST"])
def registration_form():

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        age = int(request.form.get("age", 0))

        valid = True

        if not name:
            flash("Name required", category="required")
            valid = False

        if not email:
            flash("Email required", category="required")
            valid = False

        if not age:
            flash("Age required", category="required")
            valid = False

        if "@gmail.com" not in email:
            flash("Invalid email required", category="required")
            valid = False

        if 16 > age or age > 60:
            flash("Allowed age is only 16-60", category="required")
            valid = False

        if not valid:
            return redirect(url_for("registration_form"))

        session["user"] = {
            "name": name,
            "email": email,
            "age": age,
        }
        flash("Registration successful!", category="success")

        return redirect(url_for("home_page"))

    return render_template("registration-form.html")


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5001,
    )
