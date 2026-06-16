from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crud_database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Student Class
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


@app.route("/", methods=["GET"])
def read_root():
    students = Student.query.all()
    return render_template("db_crud/index.html", students=students)


@app.route("/data/add", methods=["GET", "POST"])
def add_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        student = Student(name=name, email=email)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for("read_root"))
    return render_template("db_crud/add_data.html", students=student)


@app.route("/data/edit/<int:id>", methods=["GET", "POST"])
def update_data(id):
    student = Student.query.get_or_404(id)
    if request.method == "POST":
        student.name = request.form["name"]
        student.email = request.form["email"]
        db.session.commit()
        return redirect(url_for("read_root"))
    return render_template("db_crud/edit_data.html", student=student)


@app.route("/data/delete/<int:id>")
def delete_data(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("read_root"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
