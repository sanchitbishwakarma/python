from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = os.getenv("MAIL_PORT")
app.config["MAIL_USE_TLS"] = bool(os.getenv("MAIL_USE_TLS"))
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")

print(os.getenv("MAIL_SERVER"))
print(os.getenv("MAIL_USE_TLS"))

mail = Mail(app)

@app.route("/")
def home():
    return "This is a mail server"

@app.route("/email")
def send_email():
    msg = Message(
        subject="Flask Email Test Match",
        recipients=["sanchitbishwakarma91@gmail.com","business@sanchitbishwakarma.com.np", "shitalpoudel04@gmail.com"],
        body="This is a test message from sanchit. please ignore it. or congratulate him without any reason. 😜"
    )
    mail.send(msg)
    return "Mail sent."


if __name__ == "__main__":
    app.run(debug=True)