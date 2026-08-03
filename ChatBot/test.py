from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request


app = Flask(__name__)

bot = ChatBot("TestBot", read_only=False, 
              logic_adapters=[
                  
                  {
                      "import_path": "chatterbot.logic.BestMatch",
                      "default_response": "I am sorry, but I do not understand.",
                      "maximum_similarity_threshold": 0.90
                  }
                  ])

# List_trainer= ListTrainer(bot).train([
#     "Hello!",
#     "Hi there!",
#     "What can you do?",
#     "I can chat with you and answer your questions!",
#     "What is your name?",
#     "My name is TestBot.",
#     "What is the weather like today?",
#     "I am not sure, but you can check a weather website for the latest updates.",
#     "k xa ?",
#     "Thik xa hajur",
#     "Bye",
#     "Goodbye! Have a great day!",
# ])

# List_trainer2= ListTrainer(bot).train([
#     "Hello",
#     "हजूर",
#     "What can you do?",
#     "म एक चटबॉट हो ",
#     "What is your name?",
#     "मेरो नाम टेस्ट बोट हो .",
#     "What is the weather like today?",
#     "मलाई थाहा भएन कृपया माफ पाउ ",
#     "Bye",
#     "धन्यबाद हजूर को दिन सुभ होस!",
# ])


trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def main():
    return render_template("index.html")

# while True:
#     user_response = input("You: ")
#     bot_response = bot.get_response(user_response)
#     print("Bot:", bot_response)



@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)
