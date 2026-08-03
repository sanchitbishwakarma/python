from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

bot = ChatBot("TestBot")

# Train with English corpus
corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train("chatterbot.corpus.english")

# Optional: Custom training for English + Nepali mix
list_trainer = ListTrainer(bot)
list_trainer.train([
    "Hello!",
    "Hi there!",
    "What is your name?",
    "My name is TestBot.",
    "Bye",
    "Goodbye! Have a great day!",
    "तपाईलाई कस्तो छ ?",
    "मलाई राम्रो छ, धन्यवाद।",
])
