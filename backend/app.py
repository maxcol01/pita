from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__,
            static_folder="../frontend/static/",
            template_folder="../frontend/templates/")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/discover")
def discover():
    return render_template("discover.html")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("home"))
    else:
        return render_template("login.html")


@app.route("/register")
def register():

    return redirect(render_template("home.html"))

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=5500)