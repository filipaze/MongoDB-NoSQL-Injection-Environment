from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient

app = Flask(__name__, static_url_path='/static')

client = MongoClient("mongodb://mongo:27017/")
db = client["mydatabase"]
users = db["users"]
users.drop()
users.insert_one({"name": "admin", "password": "password"})
users.insert_one({"name": "John", "password": "john123!"})
users.insert_one({"name": "Peter", "password": "rainbow2012"})
users.insert_one({"name": "James", "password": "IAmTheBest"})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users.insert_one({"name": username, "password": password})
        success_message = "Registration successful!"
        return render_template("index.html", success_message=success_message)


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = users.find_one({"name": username, "password": password})

    if user:
        if username == "admin":
            return redirect(url_for("admin"))
        return "It would help if you tried logging in as admin. &#128521;"
    else:
        error_message = "Login failed. Incorrect username or password."
        return render_template("index.html", error_message=error_message)


@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    try:
        query = {
            "$where": f"function() {{ return this.name == '{keyword}'; }}"
        }
        results = db.users.find(query)
        results_list = [{'name': result['name'], 'password': result['password']} for result in results]


        return render_template("admin.html", search_results=results_list, keyword=keyword)
    except Exception as e:
        return render_template("admin.html", error=str(e))


@app.route("/public", methods=["GET"])
def public():
    data = list(users.find({}, {"_id": 0}))
    return jsonify(data)

@app.route("/admin", methods=["GET"])
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6543)
