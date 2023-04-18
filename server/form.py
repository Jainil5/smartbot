from flask_wtf import FlaskForm 
from wtforms import *

class Form(FlaskForm):
    text = StringField(label = "text")
    submit = SubmitField(label="submit")