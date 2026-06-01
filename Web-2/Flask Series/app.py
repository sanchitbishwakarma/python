from flask import Flask

app = Flask(__name__)

@app.route('/') # @ is decorator
def home():
    return "Hi, Sanchit the Boss"

if __name__ == '__main__':
    app.run(debug=True)