from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def default():
    return app.send_static_file('index.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    return "log page"

@app.route("/logout")
def logout():
    return "out page"

@app.route("/register")
def register():
    return "reg page"

@app.route("/user")
def user():
    return "usr page"

if __name__ == "__main__":
    app.run(debug=True)
