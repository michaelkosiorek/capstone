from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "verySecurePW"

@app.route("/hello")
def index():
    flash("What number would you like to calculate for in the series?")
    return render_template("index.html")

@app.route("/calculate", methods=["POST", "GET"])
def numberEntered():
    flash("Number entered: " + str(request.form['number_input']) + ". Number Calculated")
    return render_template("index.html")
