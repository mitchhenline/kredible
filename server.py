"""Kredible server."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
from jinja2 import StrictUndefined
import crud
from crud import get_adv_by_email, get_rep_by_email
from forms import AdvLoginForm, RepLoginForm

app = Flask(__name__)
app.secret_key= "gggc"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """view homepage."""
    return render_template("home.html")


####################### ADVOCATE LOG-IN AND LOG-OUT #############################

@app.route('/advocate')
def advocate_home():
    """view advocate homepage"""
    if 'adv_id' not in session:
        return redirect('/advocate_login')

    return render_template('advocate.html')

@app.route('/advocate_login', methods=["GET", "POST"])
def adv_login():
    """log sales advocate into site"""
    form = AdvLoginForm(request.form)

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
    
        user = crud.get_adv_by_email(email)
        if not user or user.password != password:
            flash("Invalid email or password")
            return redirect('/advocate_login')
        session['adv_id'] = user.adv_id
        return redirect('/advocate')
    return render_template("advocate_login.html", form=form)

@app.route('/adv_logout')
def adv_logout():
    del session['adv_id']
    return redirect("/advocate_login")

####################### SALES REP LOG-IN AND LOG-OUT #############################

@app.route('/rep')
def rep_home():
    """view sales rep homepage"""
    if 'rep_id' not in session:
        return redirect('/rep_login')

    return render_template('rep.html')

@app.route('/rep_login', methods=["GET", "POST"])
def rep_login():
    """log sales advocate into site"""
    form = RepLoginForm(request.form)

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = get_rep_by_email(email)
        if not user or user.password != password:
            return redirect('/rep_login')

        session['rep_id'] = user.rep_id 
        return redirect('/rep')

    return render_template("rep_login.html", form=form)

@app.route('/rep_logout')
def rep_logout():

    del session['rep_id']
    return redirect("/rep_login")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)