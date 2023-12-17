from flask import Flask,render_template,flash,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = "my_key"

class SimpleForm(FlaskForm):
    
    submit = SubmitField(label="Click Me!")

@app.route("/", methods=['GET',"POST"])
def index():

    form = SimpleForm()

    if form.validate_on_submit():
        flash("You just clicked the button")

        return redirect(url_for('index'))
    
    return render_template('3_index.html',form=form)


if __name__ == "__main__":
    app.run(debug=True)
    
