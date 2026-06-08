from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, RadioField
from wtforms.validators import DataRequired, Email, Length

class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=50)])
    gender = RadioField(label='Gender')
    submit = SubmitField('Submit')