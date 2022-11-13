from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/profile/")
def profile():
    return render_template("profile.html")

@app.route("/risks/")
def risks():
    return render_template("risks.html")

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/survey/")
def survey():
    return render_template("survey.html")

@app.route("/signup/")
def signup():
    return render_template("signup.html")
    
# @app.route("/<name>")
# def user(name):
#     return f"hello {name}!"

# @app.route("/admin/") #new page
# def admin():
#     return redirect(url_for("user", name="Admin!")) #prints out "Admin!" when page is opened


if __name__ == "__main__":
    app.run(debug = True)