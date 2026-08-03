from chatterbot import ChatBot

bot = ChatBot ("units", logic_adapters=['chatterbot.logic.UnitConversion'])

print ("............Unit Conversion.........")

while True:
    user_text= input("Ask a question (unit conversion): ")
    chatbot_response= str(bot.get_response(user_text))
    print(chatbot_response)



