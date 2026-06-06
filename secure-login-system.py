from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure Login System is Running Successfully"

users = {}
@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]

    import bcrypt
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    users[username] = hashed
    return "Registration Successful"

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username in users:
        if bcrypt.checkpw(password.encode(), users[username]):
            return "Login Successful"

    return "Invalid Credentials"

@app.route("/logout")
def logout():
    return "Logged Out"


if __name__ == "__main__":
    app.run(debug=True)

