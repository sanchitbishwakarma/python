from flask import Flask, render_template, request, jsonify, make_response
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")  # @ is decorator
def root():
    return render_template("lets_auth_it/index.html")


@app.route("/auth/login")
def authLogin():
    pass


@app.route("/auth/register")
def authRegister():
    pass


@app.route("/auth/logout")
def authLogout():
    pass


if __name__ == "__main__":
    app.run(debug=True, port=5000)
