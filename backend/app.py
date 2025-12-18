from flask import Flask, render_template, redirect, request, url_for
from  cs50 import SQL
import os
from dotenv import load_dotenv
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import re


# check if the .env files exists
load_dotenv()

# Get required env. variables
path_to_db = os.getenv("PATH_TO_DB") # path to db
SECRET_KEY = os.getenv("SESSION_SK") # secret key for session id

# create the db object
db = SQL(f"sqlite:///{path_to_db}")

# Create the app
app = Flask(__name__,
            static_folder="../frontend/static/",
            template_folder="../frontend/templates/")


# Configuration of the session
app.config["SECRET_KEY"] = SECRET_KEY # create the stamp of the session
app.config["SESSION_USE_SIGNER"] = True # prevent tempered cookies (ad to session cookie for server identification)
app.config["SESSION_TYPE"] = "filesystem" # store on the server
app.config["SESSION_PERMANENT"] = False # when the browser closes = end of session
app.config["SESSION_COOKIE_HTTPONLY"] = True # prevent XSS
app.config["SESSION_COOKIE_SAMESITE"] = "Lax" # prevent CSRF

Session(app)

# Create the routes
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
        email = request.form.get("email", None)
        password = request.form.get("password", None)
        # check if the email is in the db:
        stored_email = db.execute("SELECT email, password_hashed in users WHERE id = ?", session["id"])
        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html")


@app.route("/register", methods = ["POST","GET"])
def register():
    # check for the response type (POST/GET)
    if request.method == "POST":
        username = request.form.get("username",None)
        email = request.form.get("reg-email", None)
        password = request.form.get("reg-pwd", None)
        password_check = request.form.get("reg-pwd-cf", None)
        # check if the user entered a name
        if not username:
            # TODO: return a message of error if the user does not enter a user name
            return "error"

        # check if the user entered a valid email
        if email:
            # TODO: check if the email as a proper format
            print(f"ok:{email}")
        # check if the user entered a proper password
        if password:
            # TODO: check if the password as a proper format
            print(f"ok: {password}")
        # check if the user repeated the password correctly
        if not password_check:
            # TODO: use a function to display a message
            return redirect(url_for("login"))
        password_hashed = generate_password_hash(password)

        db.execute("INSERT INTO users (name, email, password_hashed) VALUES (?,?,?)", username, email,
                   password_hashed)
        # store the user id
        user_id = db.execute("SELECT id in users WHERE name = ?", username)
        session["user_id"] = user_id
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("login"))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":

        # For now, just redirect to the home page with a success parameter
        return redirect(url_for("home"))
    else:
        return render_template("contact.html")




if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=5500)
