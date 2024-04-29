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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab user sessions user name
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


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
        existing_user = mongo.db.users.find_one(
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


@app.route("/edit_user/<username>", methods=["GET", "POST"])
def edit_user(username):
    if request.method == "POST":
        submit = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.user.update({"username": username}, submit)
        flash("Profile Successfully Updated")
        session["user"] = request.form.get("username").lower()
        return redirect(url_for("profile", username=session["user"]))

    user = mongo.db.user.find_one({"username": username})
    return render_template("edit_user.html", user=user)


@app.route("/delete_user/<username>")
def delete_user(username):
    mongo.db.user.delete_one({"username": username})
    flash("Profile Successfully Deleted")
    session.pop("user")
    return redirect(url_for("register"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/ideas")
def ideas():
    return render_template("ideas.html")


@app.route("/get_ideas")
def get_ideas():
    idea = list(mongo.db.idea.find().sort("date", -1))
    return render_template("ideas.html", idea=idea)


@app.route("/add_ideas", methods=["GET", "POST"])
def add_ideas():
    if request.method == "POST":
        idea = {
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            "valuation": request.form.get("valuation"),
            "invest": request.form.get("invest"),
            "created_by": session["user"]
        }
        mongo.db.ideas.insert_one(idea)
        flash("Idea Successfully Added")
        return redirect(url_for("get_ideas"))

    categories = mongo.db.idea.find().sort("idea", 1)
    return render_template("ideas.html", idea=idea)


@app.route("/edit_ideas/<idea_id>", methods=["GET", "POST"])
def edit_ideas(idea_id):
    idea = mongo.db.idea.find_one({"_id": ObjectId(idea_id)})

    if request.method == "POST":
        submit = {
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            "valuation": request.form.get("valuation"),
            "invest": request.form.get("invest"),
            "created_by": session["user"]
        }
        mongo.db.idea.update({"_id": ObjectId(idea_id)}, submit)
        flash("Idea Successfully Updated")
        return redirect(url_for("get_ideas"))

    idea = mongo.db.idea.find().sort("idea", 1)
    return render_template("ideas.html", idea=idea)


@app.route("/delete_ideas/<idea_id>")
def delete_ideas(idea_id):
    mongo.db.idea.delete_one({"_id": ObjectId(idea_id)})
    flash("Idea Successfully Deleted")
    return redirect(url_for("get_ideas"))


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
