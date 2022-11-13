from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, UserSurvey
from werkzeug.security import generate_password_hash, check_password_hash
#ensures that passwords aren't stored as they actually are like x->y but y->?
from . import db
#from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, logout_user, current_user

auth= Blueprint("auth",__name__)
metadata = db.metadata

@auth.route("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("auth.survey"))
            else:
                flash("Incorrect password, try again.",category="error")
        else:
            flash("Email does not exist.", category="error") 
    return render_template("login.html", user=current_user)

@auth.route("/logout")
@login_required #requires user to be logged in to log out
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/signup", methods = ["POST","GET"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password = request.form.get("password")
        #age = request.form.get("age")
        #weight = request.form.get("weight")
        #height = request.form.get("height")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.",category="error")
        elif len(email)<4:
            flash("Email must be greater than 4 characters.",category="error")
        elif len(first_name) <2:
            flash("First name must be greater than 1 characters.",category="error")
        elif len(password) <7:
            flash("Password must be at least 7 characters long.",category="error")
        else:
            new_user = User(email=email, first_name=first_name, password = generate_password_hash(password, method="sha256"))
                #age=age,height=height,weight=weight
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created!",category="success")
            return render_template("questions.html")
    return render_template("signup.html",user=current_user)   

@auth.route("/risks")
@login_required
def risks():
    return render_template("risks.html",user=current_user)

@auth.route("/profile")
@login_required
def profile():
    return render_template("profile.html",user=current_user)

@auth.route("/questions",methods=["POST","GET"])
def survey():
    print("in survey")
    if request.method == "POST":
        print("hi")
        age = request.form.get("age")
        weight = request.form.get("weight")
        height = request.form.get("height")

        user = User.query.filter_by(id=user.id).first()
        new_UserSurvey = UserSurvey(age=age,weight=weight,height=height)
        db.session.add(new_UserSurvey)
        db.session.commit()
        flash("Information Updated!",category="success")
        return redirect(url_for("views.home",user=current_user))
    return render_template("questions.html",user=current_user)