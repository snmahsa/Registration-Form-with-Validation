from flask_wtf import FlaskForm
from wtforms import StringField, EmailField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max= 15)])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(),Length(min=8)])
    comfirm_password = PasswordField ('comfirm_password',validators=[DataRequired(),EqualTo('password')] )
    submit = SubmitField('submit')