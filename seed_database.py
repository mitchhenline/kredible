import os
from datetime import datetime
from flask import Flask
from model import db, connect_to_db, SalesAdv, SalesRep, Customer, AdvRep

app = Flask(__name__)

connect_to_db(app)

# # Drop the existing database
# try:
#     os.system("dropdb -U postgres kredible")
#     os.system("createdb -U postgres kredible")

# # Recreate the kredible database
# except:
os.system("createdb kredible")

# Creates our tables
db.create_all()

# Dummy users

# Sales Reps
rep1 = SalesRep(email = "jim@sales.com", password = "goaggies", first_name = "Jim", last_name = "Halpert", company = "Dunder Mifflin", phone_number= "505-949-8765")
rep2 = SalesRep(email = "andy@sales.com", password = "goaggies", first_name = "Andy", last_name = "Bernard", company = "Dunder Mifflin", phone_number= "505-949-0987")
rep3 = SalesRep(email = "phyllis@sales.com", password = "goaggies", first_name = "Phyllis", last_name = "Vance", company = "Dunder Mifflin", phone_number= "505-949-8322")


# Sales Advs
adv1 = SalesAdv(email = "homer@adv.com", password = "goaggies", first_name = "Homer", last_name = "Simpson", company = "Springfield Nuclear", phone_number= "090-225-3434", availability = "Tuesdays, 2pm - 5pm. Fridays, 1pm - 3pm")
adv2 = SalesAdv(email = "frodo@adv.com", password = "goaggies", first_name = "Frodo", last_name = "Baggins", company = "Shire Travel Agency", phone_number= "122-999-3774", availability = "Wednesdays, 4pm - 5pm. Thursdays, 10am - 12pm")
adv3 = SalesAdv(email = "santa@adv.com", password = "goaggies", first_name = "Santa", last_name = "Claus", company = "North Pole Gift Co.", phone_number= "152-645-0101", availability = "Mondays-Thursdays, 10am - 12pm, 4 pm - 5pm")

# Add reps and advs
db.session.add_all([
    rep1,
    rep2,
    rep3,
    adv1,
    adv2,
    adv3
])
db.session.commit()


# Dummy customers
customer1 = Customer(first_name = "Zach", last_name = "Bryan", email = "zb@music.com", company = "ZB Music", phone_number = "123-123-1234", notes = "Mr. Bryan wants to meet to get a current customer's point of view about the ticketing software.", rep_id = 1)
customer2 = Customer(first_name = "Adam", last_name = "Lazarra", email = "adam@tbsmusic.com", company = "TBS Inc.", phone_number = "123-123-1775", notes = "Adam would like more information regarding how our product has helped our customers get a better ROI.", rep_id = 1)
customer3 = Customer(first_name = "Taylor", last_name = "Swift", email = "taytay@music.com", company = "Swift Enterprises", phone_number = "123-123-9999", notes = "Ms. Swift wants to know how our software can help streamline recording.", rep_id = 1)


# Commit customers to database
db.session.add_all([customer1,customer2, customer3])
db.session.commit()

# Create connections

conn1 = AdvRep(rep_id = 1, adv_id = 1)
conn2 = AdvRep(rep_id = 1, adv_id = 2)
conn3 = AdvRep(rep_id = 1, adv_id = 3)
conn4 = AdvRep(rep_id = 2, adv_id = 2)
conn5 = AdvRep(rep_id = 3, adv_id = 2)

db.session.add_all([conn1,conn2, conn3, conn4, conn5])
db.session.commit()

