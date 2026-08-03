from chatterbot import ChatBot

bot = ChatBot("Math", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("................Mathematical chatbot ...........")

while True:
    user_text= input("Type any math equation that you want to solve: ")
    print("Testbot: " + str(bot.get_response(user_text)))