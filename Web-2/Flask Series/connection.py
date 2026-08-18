from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_connection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route("/")
def root():
    return "<a href=\"/add-multiple\">Connection Test</a>"

@app.route("/add-multiple")
def add_multiple():
    try:
        s1 = Student(name="Sanchit", email="sanchit@sanchit.ai")
        s2 = Student(name="GitHub", email="github@githu~b.com")
        db.session.add_all([s1, s2])
        db.session.commit()  # it will commit only if both data will insert successfully
        return "All students are successfully inserted."
    except:
        db.session.rollback()
        return "Error: Transaction Failed"


if __name__ == "__main__":
    with app.app_context(): 
        db.create_all()
    app.run(host="localhost", port=5002, debug=True)
