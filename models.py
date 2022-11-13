from . import db
from flask_login import UserMixin
from sqlalchemy import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id")) #must pass a valid id of existing user

#class Reminder(db.Model)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) #no user can have same email as another
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

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