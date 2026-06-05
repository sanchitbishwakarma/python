from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import DataRequired
# from wtforms import validators

class NameForm(FlaskForm):
    name = StringField('Enter your name', validators=[DataRequired()]) # , [validators.data_required()]
    submit = SubmitField('Submit')