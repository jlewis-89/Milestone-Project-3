import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/community")
def community():
    return render_template("community.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # check password hash
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid username or password
                flash("Username or password incorrect")
                return redirect(url_for("login"))
        else:
            # username doesnt match
            flash("Username or password incorrect")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/ideas")
def ideas():
    return render_template("ideas.html")


def myfunc():
    return None


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


# MONGODB CRUD OPERATIONS

# Create - db.coll.insertone({name:"jon"}) && db.coll.insertmany([{name:"jon"}, {name:"jane"}])
# Read - db.coll.findone({name:"jon"}) && db.coll.find({name:"jon"})
# Update - db.coll.updateone({name:"jon"}, {$set:{name:"jonny"}}) && db.coll.updatemany({name:"jon"}, {$set:{name:"jonny"}})
# Delete - db.coll.deleteone({name:"jonny"}) && db.coll.deletemany({name:"jonny"})
