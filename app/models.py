from . import db

class Users(db.Model):
    userid    = db.Column(db.String(100), primary_key=True)
    username  = db.Column(db.String(100), unique=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname  = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    sex   = db.Column(db.String(100), nullable=False)
    age   = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String(200), nullable=False)
    
    profile_added_on = db.Column(db.DateTime, nullable=False)
    

    def __init__(self, userid, username, firstname, lastname, sex, age, bio, image, profile_added_on):
        
        self.userid   = userid
        self.username = username
        self.firstname  = firstname
        self.lastname = lastname
        self.image  = image
        self.sex    = sex
        self.age    = age
        self.bio    = bio
        self.profile_added_on = profile_added_on

    def __repr__(self):
        return'<User %r>' % self.username