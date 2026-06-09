from flask import Flask, render_template, request, jsonify, make_response, session
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")  # @ is decorator
def root():
    return render_template("index.html")


@app.route("/cookies/set")
def setCookies():
    res = make_response("Cookies set successfully")
    res.set_cookie("PROGRAM", "BCA", max_age=100)
    return res


@app.route("/cookies/get")
def getCookies():
    res = request.cookies.get("PROGRAM") or None
    if res is None:
        return "There is no cookies related to your request."
    return res


@app.route("/cookies/del-set")
def delBySet():
    res = make_response("Cookies deleted successfully by SET.")
    res.set_cookie("PROGRAM", "", expires=0)
    return res


@app.route("/cookies/delete")
def delByDelete():
    res = make_response("Cookies deleted successfully by DELETE")
    res.delete_cookie("PROGRAM")
    return res


@app.route("/session/set")
def setSession():
    session["username"] = "Sanchit"
    return "Logged in!"


@app.route("/session/get")
def getSession():
    username = session.get("username")
    return f"Logged in as '{username}'"


@app.route("/session/del")
def delSession():
    session.pop("username", None)
    return "Logged out!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
