from final import create_app #,render_template

app = create_app()

#@app.route("home")
#def home():
#    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)