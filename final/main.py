from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFCATIONS"] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        
    def __repr__(self):
        return self.username

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/logout")
def logout():
    return render_template("home.html")

@app.route("/diabetes")
def diabetes():
    return render_template("home.html")

@app.route("/survey", methods=["POST", "GET"])
def survey():
    return render_template("survey.html")

if __name__ == "__main__":
    app.run(debug=True)