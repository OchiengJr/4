from wtforms import Form, StringField, validators
from models import Hero, Power  # Import your database models

class HeroPowerForm(Form):
    strength = StringField('Strength', [validators.InputRequired(), validators.AnyOf(['Strong', 'Weak', 'Average'])])

class PowerForm(Form):
    description = StringField('Description', [validators.InputRequired(), validators.Length(min=20)])
