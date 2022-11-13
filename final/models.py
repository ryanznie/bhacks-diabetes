from . import db
from flask_login import UserMixin

#class Reminder(db.Model)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) #no user can have same email as another
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # age = db.Column(db.Integer)
    # weight = db.Column(db.Integer)
    # height = db.Column(db.Integer)

class UserSurvey(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)

    #smoker = db.Column(db.Boolean)
    #stroke = db.Column(db.Boolean)
    #highbp = db.Column(db.Boolean)
    #bloodchol = db.Column(db.Boolean)
    #notes = db.relationship("Note") #lists all of different notes that user has