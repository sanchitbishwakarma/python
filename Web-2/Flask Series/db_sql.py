from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # to suppress warning

db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


@app.route("/")
def home():
    return "asd"


@app.route("/database/add")
def add_student():
    name = request.args.get('name')
    email = request.args.get('email')
    student = Students(name=name, email=email)
    db.session.add(student)
    db.session.commit()
    return "Student added to our database!"


@app.route("/database/students")
def show_students():
    students = Students.query.all()
    if not students:
        return "No Data available."
    return "<br>".join([f"{std.id}. {std.name} -> {std.email}" for std in students])


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
