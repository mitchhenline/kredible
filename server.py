"""Kredible server."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
from jinja2 import StrictUndefined
from crud import create_user, get_user_by_email
from forms import LoginForm

app = Flask(__name__)
app.secret_key= "gggc"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """view homepage."""
    if 'email' not in session:
        return redirect('/login')
    #elif email.user not 

    return render_template('home.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    """log user into site"""
    form = LoginForm(request.form)

    # Form is submitted with valid data
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

    #Check to see if a user with this email exists
        user = crud.get_user_by_email(email)

        if not user or user.password != password:
            # add flash later--flash("Invalid email or password")
            return redirect('/login')

        session['email'] = user.email
        return redirect('/')

    return render_template("login.html", form=form)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)