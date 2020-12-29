from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegistrationForm(FlaskForm):
    """
    This Class represents the form, this will be used to make the actual html form
    """
    username = StringField(label="Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo(fieldname='password')])
    submit = SubmitField(label="Sign Up")


class LoginForm(FlaskForm):
    """
    This Class represents the form, this will be used to make the actual html form
    """
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember = BooleanField(label="Remember Me")
    submit = SubmitField(label="Login")