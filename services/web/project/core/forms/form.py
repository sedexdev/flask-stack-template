
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError

from project.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=6, max=128)])
    password = PasswordField('Password', validators=[
        InputRequired(),
        Length(min=12, max=128)
    ])
    remember = BooleanField("Remember me")

    
class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired(), Length(min=6, max=128)])
    password = PasswordField('Password', validators=[
        InputRequired(),
        Length(min=12, max=128)
    ])
    confirm_password = PasswordField('Confirm password', validators=[
        InputRequired(),
        Length(min=12, max=128)
    ])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')
