from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!<h1>"

@app.route("/puppy_latin/<name>")
def puppy_latin(name):

    if name[-1].lower() == 'y':
        name_latin = name[:-1]+"iful"
    else:
        name_latin = name+'y'
    
    return f"<h1>Hi {name}!. Your puppy latin name is {name_latin}<h1/>"

if __name__ == '__main__':
    app.run(debug=True)