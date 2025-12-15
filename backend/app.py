from flask import Flask, render_template, redirect, request, url_for
import sqlite3
from  cs50 import SQL
import os
from dotenv import load_dotenv

# check if the .env files exists
load_dotenv()

# create the path to the db
path_to_db = os.getenv("PATH_TO_DB")

# create the db object
db = SQL(f"sqlite:///{path_to_db}")

app = Flask(__name__,
            static_folder="../frontend/static/",
            template_folder="../frontend/templates/")

@app.route("/")
def home():
    return render_template("home.html")



@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/discover")
def discover():
    return render_template("discover.html")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html")


@app.route("/register")
def register():

    return redirect(render_template("dashboard.html"))

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # In a real application, you would process the form data here
        # For example, send an email or store the message in a database
        # name = request.form.get("name")
        # email = request.form.get("email")
        # subject = request.form.get("subject")
        # message = request.form.get("message")

        # For now, just redirect to the home page with a success parameter
        return redirect(url_for("home"))
    else:
        return render_template("contact.html")




if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=5500)
