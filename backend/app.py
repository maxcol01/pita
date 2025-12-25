from flask import Flask, render_template, redirect, request, url_for, session, flash
from  cs50 import SQL
import os
from dotenv import load_dotenv
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_wtf.csrf import CSRFProtect

# check if the .env files exists
load_dotenv()

# Get required env. variables
path_to_db = os.getenv("PATH_TO_DB") # path to db
SECRET_KEY = os.getenv("SESSION_SK") # secret key for session id
AI_API_KEY = os.getenv("OPEN_AI_KEY")

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

# Protection against CSRF

#csrf = CSRFProtect(app)


# Categories

categories = [
    "Vegetables",
    "Fruits",
    "Meat & Fish",
    "Dairy & Alternatives",
    "Bakery & Grains",
    "Canned & Jarred",
    "Frozen Foods",
    "Condiments & Sauces",
    "Spices & Seasonings",
    "Snacks & Sweets",
    "Nuts, Seeds & Spreads",
    "Beverages",
    "Other"
]

# Create the additional layer of protection using the header
@app.after_request
def header_security_definition(response):
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

### Create the routes ###
@app.route("/")
def home():
    return render_template("home.html")



@app.route("/dashboard")
def dashboard():
    # Check if user is logged in
    if not session.get("user_id"):
        return redirect(url_for("login"))
    user_items = db.execute("SELECT * FROM pantry_items WHERE user_id = ?", session["user_id"])
    print(user_items)
    return render_template("dashboard.html", name=session["name"], user_items=user_items)

@app.route("/discover")
def discover():
    return render_template("discover.html")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        # Get form data
        email = request.form.get("email", None)
        password = request.form.get("password", None)

        # Basic validation
        if not email:
            flash(message="Email is required", category="error")
            return redirect(url_for("login"))

        if not password:
            flash(message="Password is required", category="error")
            return redirect(url_for("login"))

        # Check if the email exists in the database
        user = db.execute("SELECT * FROM users WHERE email = ?", email)

        # If no user found or password is incorrect
        if not user or not check_password_hash(user[0]["password_hashed"], password):
            flash(message="Invalid email or password", category="error")
            return redirect(url_for("login"))

        # Extract relevant information: Set up the session + name of the user
        session["user_id"] = user[0]["id"]
        session["name"] = user[0]["name"]
        #print(session["name"])
        # Redirect to dashboard
        flash(message=f"Welcome {session["name"]}", category="success")
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

        # Check if the user entered a name
        if not username:
            flash(message="Username is required", category="error")
            return redirect(url_for("login.html"))

        # Check if the user entered a valid email
        if not email:
            flash(message="Email is required")
            return redirect(url_for("login.html"))

        # Check if email already exists
        existing_user = db.execute("SELECT * FROM users WHERE email = ?", email)
        if existing_user:
            flash(message="Email already registered", category="error")
            return redirect(url_for("login.html"))

        # Check if the user entered a password
        if not password:
            flash(message="Password is required", category="error")
            return redirect(url_for("login.html"))
        # Check if password is at least 6 characters
        if len(password) < 6:
            flash(message="Password must be at least 6 characters", category="error")
            return redirect(url_for("login.html"))
        # Check if the passwords match
        if password != password_check:
            flash(message="Passwords do not match", category="error")
            return redirect(url_for("login.html"))
        # Hash the password
        password_hashed = generate_password_hash(password)

        # Insert the new user into the database
        db.execute("INSERT INTO users (name, email, password_hashed) VALUES (?,?,?)", 
                  username, email, password_hashed)

        # Get the user ID and store it in the session + name of user for welcoming message.
        response = db.execute("SELECT name, id FROM users WHERE email = ?", email)
        session["user_id"] = response[0]["id"]
        session["name"] = response[0]["name"]
        # Redirect to dashboard
        flash(message=f"Welcome {session["name"]}", category= "success")
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("login"))


@app.route("/edit-item")
def edit_item():

    return render_template("item_definition.html", categories=categories)


@app.route("/add-item", methods = ["POST", "GET"])
def add_item():
    if request.method == "POST":
        item_name = request.form.get("name")
        item_category = request.form.get("category")
        item_quantity = request.form.get("quantity")
        item_unit = request.form.get("unit")
        item_exp_date = request.form.get("exp-date")
        item_location = request.form.get("location")

        db.execute("INSERT INTO pantry_items (user_id, name, category, quantity, unit, expiration_date, location) VALUES (?, ?, ?, ?, ?, ?, ?)", session["user_id"], item_name, item_category, item_quantity, item_unit, item_exp_date, item_location)
        return redirect(url_for("dashboard"))
    else:
        return render_template("item_definition.html", categories=categories)

@app.route("/delete-item")
def delete_item():
    pass

@app.route("/my-assistant")
def ai_assistant():
    return render_template("assistant.html")

@app.route("/logout")
def logout():
    # Clear the session
    session.clear()
    # Redirect to home page
    return redirect(url_for("home"))

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
