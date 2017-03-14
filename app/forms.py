from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.fields import TextField, TextField, RadioField
from wtforms.fields.html5 import IntegerField
from wtforms.validators import Required, NumberRange, ValidationError
from app import db
from app.models import Users
from sqlalchemy.sql import exists


def validate_username(form,field):
    if db.session.query(exists().where(Users.username == field.data)).scalar():
        raise ValidationError('Username already exists.')

class UserProfileForm(Form):
    username  = TextField('Username:', validators=[Required(), validate_username])
    firstname = TextField('First Name:', validators=[Required()])
    lastname  = TextField('Last Name:', validators=[Required()])
    sex       = RadioField('Sex:', validators=[Required()], choices=[('M','M'),('F','F')])
    age       = IntegerField('Age:', validators=[Required(),NumberRange(min=0, max=100)])
    bio        =TextField("Biography", validators = [Required()])
    img       = FileField('Image:', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
    
    

    