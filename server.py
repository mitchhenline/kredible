"""Kredible server."""

from flask import Flask, render_template, request, flash, session, redirect, abort
from model import connect_to_db, db, Customer, Meeting
from jinja2 import StrictUndefined
import crud
from forms import AdvLoginForm, RepLoginForm, AddCustomer, RequestMeeting

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

    relationships = crud.get_relationships_by_adv_id(session['adv_id'])
    user = crud.get_adv_by_adv_id(session['adv_id'])
    meetings = crud.get_meetings_by_adv_id(session['adv_id'])

    sales_reps = []
    for relationship in relationships:
        sales_reps.append(relationship.sales_rep)

    return render_template('advocate.html', sales_reps = sales_reps, user = user, meetings = meetings)

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

@app.route('/register')
def register():
    return render_template('/register.html')

####################### SALES REP LOG-IN AND LOG-OUT, HOME PAGE #############################

@app.route('/rep')
def rep_home():
    """view sales rep homepage"""
    if 'rep_id' not in session:
        return redirect('/rep_login')

    form = AddCustomer(request.form)
    customers = crud.get_customers_by_rep_id(session['rep_id'])
    user = crud.get_rep_by_rep_id(session['rep_id'])
    relationships = crud.get_relationships_by_rep_id(session['rep_id'])
    sales_advs = []
    meetings = crud.get_meetings_by_rep_id(session['rep_id'])

    for relationship in relationships:              #grabs the sales advocates from the relationship and puts into list
        sales_advs.append(relationship.sales_adv)

    return render_template('rep.html', sales_advs = sales_advs, customers = customers, user = user, form = form, meetings = meetings)

@app.route('/rep', methods =['POST'])
def add_customer():
    """add customer"""
    form = AddCustomer(request.form)
    if 'rep_id' not in session:
        return redirect('/rep_login')
    if form.validate_on_submit():
        customer = Customer(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            company = form.company.data,
            phone_number = form.phone_number.data,
            notes = form.notes.data,
            rep_id = session['rep_id']
        )
        db.session.add(customer)
        db.session.commit()
        return redirect('/rep')
    else:
        abort(404)

@app.route('/rep_login', methods=["GET", "POST"])
def rep_login():
    """log sales advocate into site"""
    form = RepLoginForm(request.form)

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = crud.get_rep_by_email(email)
        if not user or user.password != password:
            return redirect('/rep_login')

        session['rep_id'] = user.rep_id 
        return redirect('/rep')

    return render_template("rep_login.html", form=form)

@app.route('/rep_logout')
def rep_logout():

    del session['rep_id']
    return redirect("/rep_login")

####################### ADVOCATE VIEW INDIVIDUAL REP PAGE #############################

@app.route('/advocate/<rep_id>')
def view_ind_rep(rep_id):
    """view advocate's rep information'"""
    if 'adv_id' not in session:
        return redirect('/advocate_login')

    messages = crud.get_messages_by_rep_id(rep_id)
    message_list = []
    for message in messages:
        message_list.append(message.message)

    rep = crud.get_rep_by_rep_id(rep_id)
    return render_template('view_ind_rep.html', message_list = message_list, rep = rep)

####################### SALES REP VIEW INDIVIDUAL ADV PAGE #############################

@app.route('/rep/<adv_id>', methods=['GET'])
def view_ind_adv(adv_id):
    """view sales rep's advocate information'"""
    if 'rep_id' not in session:
        return redirect('/rep_login')

    messages = crud.get_messages_by_adv_id(adv_id)
    message_list = []
    for message in messages:
        message_list.append(message.message)
    
    adv = crud.get_adv_by_adv_id(adv_id)
    form = RequestMeeting(request.form)
    return render_template('view_ind_adv.html', message_list = message_list, adv = adv, form = form)

@app.route('/rep/<int:adv_id>', methods=['POST'])
def request_meeting(adv_id):
    """view sales rep's advocate information'"""
    if 'rep_id' not in session:
        return redirect('/rep_login')
    adv = crud.get_adv_by_adv_id(adv_id)

    form = RequestMeeting(request.form)
    if form.validate_on_submit():
        meeting = Meeting(
            date = form.date.data,
            time = form.time.data,
            meeting_link = form.meeting_link.data,
            meeting_prep_notes = form.meeting_prep_notes.data,
            meeting_accepted = False,
            cust_id = form.cust_id.data,
            adv_id = adv_id,
            rep_id = session['rep_id']
        )
        print("made it through validate form")
        db.session.add(meeting)
        db.session.commit()
        return redirect(f'/rep/{adv_id}')
    else:
        print(form.errors)

    messages = crud.get_messages_by_adv_id(adv_id)
    message_list = []
    for message in messages:
        message_list.append(message.message)
    
    print('FORM DID NOT VALIDATE')
    return render_template('view_ind_adv.html', form = form, adv = adv, message_list = message_list)

####################### SALES REP VIEW INDIVIDUAL MEETING PAGE #############################

@app.route('/rep/meeting/<meeting_id>')
def view_ind_mtg(meeting_id):
    """view meeting information"""
    if 'rep_id' not in session:
        return redirect('/rep_login')

    meeting = crud.get_meeting_by_meeting_id(meeting_id)
    return render_template('view_ind_meeting.html', meeting = meeting)

####################### SALES ADV VIEW INDIVIDUAL MEETING PAGE #############################

@app.route('/adv/meeting/<meeting_id>')
def view_ind_mtg_as_adv(meeting_id):
    """view meeting information"""
    if 'adv_id' not in session:
        return redirect('/adv_login')

    meeting = crud.get_meeting_by_meeting_id(meeting_id)
    return render_template('view_ind_meeting_as_adv.html', meeting = meeting)


####################### SALES REP VIEW PROSPECT PAGE #############################

@app.route('/rep/customer/<cust_id>')
def view_ind_cust(cust_id):
    """view customer information"""
    if 'rep_id' not in session:
        return redirect('/rep_login')

    customer = crud.get_customer_by_cust_id(cust_id)
    return render_template('view_ind_cust.html', customer = customer)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)