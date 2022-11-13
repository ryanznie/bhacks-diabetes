from final import create_app #,render_template

app = create_app()

@app.route("home")
def home():
    return render_template("home.html")

@app.route("login")
def home():
    return render_template("login.html")

@app.route("profile")
def home():
    return render_template("profile.html")

@app.route("logout")
def logout():
    return render_template("home.html")

@app.route("diabetes")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)