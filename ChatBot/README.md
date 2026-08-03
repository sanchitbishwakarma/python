# 🤖 Chatbot Practice Project

![Chatbot Example](ChatBot_Example.png) 
This is a simple chatbot built using **Python**, **Flask**, and **ChatterBot**. It supports Engish and runs through a clean web interface.

---

## ✅ Requirements

Before running the chatbot, ensure the following:

1. Latest python or python 3.7 or 3.10 should be installed 
2. Terminal or CMD access

Check Python installation:
```bash
python --version
pip --version

📦 Installation Steps
Install all necessary packages by running in cmd:

pip install flask
pip install chatterbot
pip install git+https://github.com/gunthercox/chatterbot-corpus.git
pip install spacy
pip install pyyaml
pip install pint
pip install jupyter
pip install notebook
python -m spacy download en

# If chatterbot fails from PyPI, install directly from GitHub:
pip install git+https://github.com/gunthercox/ChatterBot.git

## 🚀 How to Run the Project
1. Train the Chatbot (first time only)
python train.py

2. Start the Web Server
python main.py

3. Open in Browser
Go to:
http://127.0.0.1:5000/


ℹ️ Notes
--ChatterBot is compatible with Python 3.7–3.10
--Trained data is stored locally (typically in db.sqlite3)
--No need to retrain every time — only run train.py again when you change the training data

