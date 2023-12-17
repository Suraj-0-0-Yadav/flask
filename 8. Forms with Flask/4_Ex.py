from flask import Flask, render_template,session,flash,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = "mykey"

class Info(FlaskForm):

    breed = StringField(label="What Breed are you ?")
    submit = SubmitField(label="Submit")

@app.route("/", methods=['GET','POST'])
def index():

    form = Info()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just change the breed to : {session['breed']} ")

        return redirect(url_for('index'))
    
    return render_template('4_index.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)