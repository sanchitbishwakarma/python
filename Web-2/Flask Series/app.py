from flask import Flask, render_template, request, jsonify, redirect, make_response
from form import NameForm
from flask_mail import Mail, Message
from send_email import EmailFormClass
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
app.config["UPLOAD_FOLDER"] = "static/uploads"


@app.route("/")  # @ is decorator
def root():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return f"Hello, {name}!"


@app.route("/wt-form", methods=["GET", "POST"])
def formFunction():
    error = None
    form = NameForm()
    if form.validate_on_submit():
        return f"<p>I got to know that your name is {form.name.data}, and your email is {form.email.data}</p>"
    return render_template("wt-form.html", form=form)


app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")

mail = Mail(app)

print(app.config["MAIL_SERVER"])
print(app.config["MAIL_PORT"])
print(app.config["MAIL_USERNAME"])


@app.route("/email/send", methods=["GET", "POST"])
def emailForm():
    emailForm = EmailFormClass()

    if emailForm.validate_on_submit():
        data = {
            "subject": emailForm.e_subject.data,
            "recipients": emailForm.e_recipients.data,
            "message": emailForm.e_message.data,
            "attachment": emailForm.e_attachment.data,
        }

        res = sendMail(data)

        if res is None:
            return redirect("/email/success")
        else:
            return redirect("/email/error")

    return render_template("send_email.html", form=emailForm)


def sendMail(data):
    msg = Message(
        subject=data["subject"].strip(),
        recipients=[email.strip() for email in data["recipients"].split(",")],
        body=data["message"].strip(),
    )

    attachment = data["attachment"]
    if attachment:
        filename = attachment.filename
        attachment.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        with app.open_resource(
            os.path.join(app.config["UPLOAD_FOLDER"], filename)
        ) as fp:
            msg.attach(filename, attachment.content_type, fp.read())
        os.remove(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    return mail.send(msg)


@app.route("/email/success")
def emailSuccess():
    return render_template("email_success.html")


@app.route("/email/error")
def emailError():
    return render_template("email_error.html")


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
def delByEte():
    res = make_response("Cookies deleted successfully by DELETE")
    res.delete_cookie("PROGRAM")
    return res


if __name__ == "__main__":
    app.run(debug=True, port=5173)
