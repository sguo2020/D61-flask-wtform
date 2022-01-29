from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    return render_template('login2.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)