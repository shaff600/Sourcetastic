import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
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
@app.route("/get_resources")
def get_resources():
    resources = mongo.db.resources.find()
    return render_template("resources.html", resources=resources)


@app.route("/register", methods=["GET", "POST"])
def register():
    """method used to register a new user"""
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
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
        return redirect(url_for("get_resources", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "get_resources", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/add_resources", methods=["GET", "POST"])
def add_resources():
    if request.method == "POST":
        submit_resource = {
            "name": request.form.get("name"),
            "category_name": request.form.get("category_name"),
            "link": request.form.get("link"),
            "description": request.form.get("description"),
            "created_by": session["user"]
        }

        mongo.db.resources.insert_one(submit_resource)
        flash("Resource added succesfully")
        return redirect(url_for("get_resources", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_resources.html", categories=categories)



@app.route("/edit_resources/<resource_id>", methods=["GET", "POST"])
def edit_resources(resource_id): 
    if request.method == "POST":
        edit_resource = {
            "name": request.form.get("name"),
            "category_name": request.form.get("category_name"),
            "link": request.form.get("link"),
            "description": request.form.get("description"),
            "created_by": session["user"]
        }

        mongo.db.resources.update({"_id": ObjectId(resource_id)}, edit_resource)
        flash("Resource Succesfully Updated")
        return redirect(url_for("get_resources", username=session["user"]))

    resource = mongo.db.resources.find_one({"_id": ObjectId(resource_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_resources.html", resource=resource, categories=categories)



@app.route("/delete_resource/<resource_id>")
def delete_resources(resource_id):
    mongo.db.resources.remove({"_id": ObjectId(resource_id)})
    flash("Resource Deleted")
    return redirect(url_for("get_resources"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name",1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)