from flask import Flask

app = Flask(__name__)

@app.route("/")  # 127.0.0.1:5000
def index():
    return "<h1>Hello World<h1/>"

@app.route("/information")  # 127.0.0.1:5000/information
def information():
    return "<h1>Get information here !!!<h1/>"


@app.route("/puppy/<name>")
def puppy(name):
    return f"<h1>This is page for {name.upper()}<h1/>"

@app.route("/get100/<name>")
def get100(name):
    return f"100th letter is {name[0]}"

if __name__ == "__main__":
    app.run(debug=True)