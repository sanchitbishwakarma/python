from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError

# @app.route('/send-mail')
# def sendMail():
#     msg = Message(
#         subject='Namaster ji',
#         recipients=['sashilal120@gmail.com', 'shitalpoudel04@gmail.com', 'sanchitbishwakarma91@gmail.com'],
#         body='bulla di jana mai kon, mogambo khush hua, you are too cute buddy,  TAKE RISK NOW AND DO SOMETHING BOLD YOU WON\'t REGRET IT'
#     )
#     mail.send(msg)
#     return 'Email sent succesfully!'

class EmailFormClass(FlaskForm):
    e_recipients = StringField(label='Recipients', description='Enter your recipients with coma(,) separated',validators=[DataRequired(), Email()])
    e_subject = StringField("Subject",description="Enter the subject of the email",validators=[Length(min=3,max=100)])
    e_message = TextAreaField("Message", description="Write the message", validators=[Length(min=5)])
    e_attachment = FileField("Attachment", description="Add a attachment", validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], "Only images and pdf files are allowed")])
    e_submit = SubmitField("Send Mail", description="Want to send the mail")
    