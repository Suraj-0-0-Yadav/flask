from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    my_list = [1,2,3,4,5]
    puppies = ['Fluffy', 'Rufus', 'Spike']
    return render_template('3_template_control_flow.html',
                           my_list=my_list,
                           puppies=puppies)

@app.route("/get_table/<n>")
def get_table(n):
    return render_template("table.html",n=int(n))

if __name__ == '__main__':
    app.run(debug=True)

