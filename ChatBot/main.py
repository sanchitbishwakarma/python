from chatterbot import ChatBot
from flask import Flask, render_template, request
# from flask_cors import CORS  # Uncomment if you need CORS support

app = Flask(__name__)
# CORS(app)  # Uncomment if frontend is separate or hosted elsewhere

bot = ChatBot("TestBot", read_only=True, 
              logic_adapters=[
                  {
                      "import_path": "chatterbot.logic.BestMatch",
                      "default_response": "I am sorry, but I do not understand.",
                      "maximum_similarity_threshold": 0.90
                  }
              ])

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get")
def get_chatbot_response():
    user_text = request.args.get('userMessage')
    return str(bot.get_response(user_text))

if __name__ == "__main__":
    app.run(debug=True)
