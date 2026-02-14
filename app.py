from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/destinations")
def destination():
    return render_template("destinations.html")

@app.route("/restaurants")
def restaurant():
    return render_template("restaurants.html")

@app.route("/homestays")
def homestays():
    return render_template("homestays.html")

@app.route("/safety")
def safety():
    return render_template("safety.html")

@app.route("/alert")
def alert():
    return render_template("alert.html")

@app.route("/budget")
def budget():
    return render_template("budget.html")

if __name__ == "__main__":

    app.run(debug=True)
