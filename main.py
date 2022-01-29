from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, email
from flask_bootstrap import Bootstrap

app = Flask(__name__)


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'letsdance'


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), email()])
    password = PasswordField('Password', validators=[DataRequired(message="minimum 8 characters"), Length(min=8)])
    submit = SubmitField('log In')


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login2.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
