from flask import Blueprint, render_template

auth= Blueprint("auth",__name__)

@auth.route("/login", methods = ["POST","GET"])
def login():
    return render_template("login.html",boolean=True)

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/signup", methods = ["POST","GET"])
def signup():
    return render_template("signup.html")   
