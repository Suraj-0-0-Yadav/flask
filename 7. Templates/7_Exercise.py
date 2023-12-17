from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("7_index.html")

@app.route('/report')
def report():

    lower_letter = False
    upper_letter = False
    num_end = False

    username = request.args.get('username')

    lower_letter = any(ch.islower() for ch in username)
    upper_letter = any(ch.isupper() for ch in username)
    num_end = username[-1].isdigit()

    report = lower_letter and upper_letter and num_end

    return render_template('7_report.html',
                           report=report,
                           lower_letter=lower_letter,
                           upper_letter=upper_letter,
                           num_end=num_end)


if __name__ == '__main__':
    app.run(debug=True)

