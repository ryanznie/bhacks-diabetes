from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import User
from . import db
#import json

views= Blueprint("views",__name__)

@views.route("/",methods=["GET","POST"])
@login_required

def home():
    return render_template("home.html",user=current_user)

#@views.route("/survey",methods=["POST","GET"])
#@login_required    
#def survey():
#    if request.method == "POST":
#        age = request.form.get("age")
#        weight = request.form.get("weight")
#        height = request.form.get("height")

#        def __init__(self,age,weight,height):
#            self.age = age
#            self.weight = weight
#            self.height = height

#        db.session.commit()
#    return render_template("home.html",user=current_user)