from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm

from wtforms import (StringField,BooleanField,
                     DateField,RadioField,SelectField,
                     TextAreaField,SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecretkey"

class InfoForm(FlaskForm):

    breed = StringField(label="What breed are you ?",validators=[DataRequired()])
    neutered = BooleanField(label="have you been neutered ?")
    mood = RadioField(label="Please choose you mood ?",
                      choices=[("mood_one","Happy"),("mood_two","Exicited")])
    food_list = SelectField(label="Pick you favorite food ?",
                            choices=[('chi','Chicken'),('bf','beef'),('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField(label="Submit")

@app.route("/", methods=['GET','POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():

        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_list.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))
    
    return render_template('2_index.html', form=form)

@app.route("/thankyou")
def thankyou():
    return render_template('2_thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)