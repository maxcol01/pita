from flask import Flask, render_template, redirect, request, url_for
from  cs50 import SQL
import os
from dotenv import load_dotenv
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash




# check if the .env files exists
load_dotenv()

# create the path to the db
path_to_db = os.getenv("PATH_TO_DB")
SECRET_KEY = os.getenv("SESSION_SK")
# create the db object
db = SQL(f"sqlite:///{path_to_db}")


# Create the app
app = Flask(__name__,
            static_folder="../frontend/static/",
            template_folder="../frontend/templates/")


# Configuration of the session
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SESSION_TYPE"] = "filesystem" # store on the server
app.config["SESSION_PERMANENT"] = False # when the browser closes = end of session
app.config["SESSION_USE_SIGNER"] = True # prevent tempered cookies
app.config["SESSION_COOKIE_HTTPONLY"] = True # prevent XSS
app.config["SESSION_COOKIE_SAMESITE"] = "Lax" # prevent CSRF

Session(app)

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


@app.route("/register", methods = ["POST","GET"])
def register():
    # check for the response type (POST/GET)
    if request.method == "POST":
        username = request.form.get("username",None)
        email = request.form.get("reg-email", None)
        password = request.form.get("reg-pwd", None)
        password_check = request.form.get("reg-pwd-cf", None)
        # check if the user entered a name
        if username:
            print(f"ok: {username}")

        # check if the user entered a valid email
        if email:
            print(f"ok:{email}")
        # check if the user entered a proper password
        if password:
            print(f"ok: {password}")
        # check if the user repeated the password correctly
        if password_check:
            print(f"ok: {password_check}")
            password_hashed = generate_password_hash(password)
        if username and email and password and (password_check == password):
            print("we can login")

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
