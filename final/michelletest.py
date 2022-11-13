from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/")
def login():
    return "hellohellohello"

@app.route("/<name>")
def profile(name):
    return render_template("index.html",content=name) #pass value to html
    
# @app.route("/<name>")
# def user(name):
#     return f"hello {name}!"

# @app.route("/admin/") #new page
# def admin():
#     return redirect(url_for("user", name="Admin!")) #prints out "Admin!" when page is opened


if __name__ == "__main__":
    app.run(debug = True)