from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length, NumberRange, DataRequired, ValidationError
from fakeshop.models import Postcode

class PostcodeHouseholdForm(FlaskForm):
    postcode = StringField("What's your postcode?",
                            validators=[DataRequired(), Length(min=3, max=10)])
    household = IntegerField("How many are in your household?",
                            validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField("See your shopping basket")

    # checks if postcode exists
    def validate_postcode(self, postcode):
        print('inside class')
        postcode = Postcode.query.filter_by(postcode=postcode.data).first()
        if not postcode:
            raise ValidationError('This postcode does not exist in out database. Choose another one.')

