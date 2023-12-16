from flask import Flask

app = Flask(__name__)

@app.route("/")  # 127.0.0.1:5000
def index():
    return "<h1>Hello World<h1/>"

@app.route("/information")  # 127.0.0.1:5000/information
def information():
    return "<h1>Get information here !!!<h1/>"

if __name__ == "__main__":
    app.run()