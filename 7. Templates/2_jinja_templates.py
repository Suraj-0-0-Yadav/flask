from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    my_name = "Suraj"
    letters = list(my_name)
    my_dict = {'Name':"Suraj",
               'Lang': "Hindi"}
    return render_template('2_jinja_template.html', 
                           my_name=my_name,
                           letters=letters,
                           my_dict=my_dict)


if __name__ == '__main__':
    app.run(debug=True)

