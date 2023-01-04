"""Kredible server."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
from jinja2 import StrictUndefined
from crud import create_sales_rep, get_user_by_email
from forms import AdvLoginForm, RepLoginForm

app = Flask(__name__)
app.secret_key= "gggc"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """view homepage."""
    return render_template("home.html")

@app.route('/advocate')
def advocate_home():
    """view advocate homepage"""
    if 'email' not in session:
        return redirect('/advocate_login')

@app.route('/advocate_login', methods=["GET", "POST"])
def adv_login():
    """log sales advocate into site"""
    form = AdvLoginForm(request.form)

    # Form is submitted with valid data
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

    #Check to see if a user with this email exists
        user = get_user_by_email(email)

        if not user or user.password != password:
            flash("Invalid email or password")
            return redirect('/advocate_login')

        session['email'] = user.email 
        return redirect('/advocate')

    return render_template("advocate_login.html", form=form)

@app.route('/rep')
def rep_home():
    """view sales rep homepage"""
    if 'email' not in session:
        return redirect('/rep_login')

@app.route('/rep_login', methods=["GET", "POST"])
def rep_login():
    """log sales advocate into site"""
    form = RepLoginForm(request.form)

    # Form is submitted with valid data
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

    #Check to see if a user with this email exists
        user = get_user_by_email(email)

        if not user or user.password != password:
            flash("Invalid email or password")
            return redirect('/rep_login')

        session['email'] = user.email 
        return redirect('/rep')

    return render_template("rep_login.html", form=form)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)