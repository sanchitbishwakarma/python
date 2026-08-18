# initial app
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

# database url config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db Initialize
db = SQLAlchemy(app)


# setup the database table
class Student(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)


# create
@app.route("/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()

        new_user = Student(name=name, age=age)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("home_page"))
    return render_template("create_user.html")


# read
@app.route("/read", methods=["GET"])
def home_page():
    users = Student.query.all()
    return render_template("home_page.html", users=users)


# start engine
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="localhost", debug=True, port=5002)
