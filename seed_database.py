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
adv1 = SalesAdv(email = "carl@adv.com", password = "goaggies", first_name = "Carl", last_name = "Carlson", company = "Springfield Nuclear", phone_number= "090-225-3434", availability = "Tuesdays, 2pm - 5pm. Fridays, 1pm - 3pm")
adv2 = SalesAdv(email = "lenny@adv.com", password = "goaggies", first_name = "Lenny", last_name = "Leonard", company = "Springfield Nuclear", phone_number= "122-999-3774", availability = "Wednesdays, 4pm - 5pm. Thursdays, 10am - 12pm")
adv3 = SalesAdv(email = "moe@adv.com", password = "goaggies", first_name = "Moe", last_name = "Syzlak", company = "Moe's Tavern", phone_number= "152-645-0101", availability = "Mondays-Thursdays, 10am - 12pm, 4 pm - 5pm")

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
customer1 = Customer(first_name = "Soleil", last_name = "Byrtus", email = "sb@bodhi.com", company = "ZB Music", phone_number = "123-123-1234", notes = "Soleil wants to meet to get a current customer's point of view about the ticketing software.", rep_id = 1)
customer2 = Customer(first_name = "Matt", last_name = "Gawlik", email = "itschewsday@roight.com", company = "Cleveland Construction", phone_number = "123-123-1775", notes = "Matt would like more information regarding how our product has helped our customers get a better ROI.", rep_id = 1)
customer3 = Customer(first_name = "Harry", last_name = "Colyer", email = "harry@vermont.com", company = "Harold Inc.", phone_number = "123-123-9999", notes = "Harry wants to know how our software can help streamline customer service processes.", rep_id = 1)
customer4 = Customer(first_name = "Amelia", last_name = "Stimpson", email = "astimpson@luvrq.com", company = "RQ", phone_number = "123-123-4499", notes = "Amelia is interested in purchasing, but she would like to get a current customer's review on how it has benefitted their org.", rep_id = 1)
customer5 = Customer(first_name = "Cole", last_name = "DeSilvia", email = "icecole@cybersecurity.com", company = "Big Time Cyber", phone_number = "123-123-9049", notes = "Cole wants to know how our software can help streamline customer service processes.", rep_id = 1)
customer6 = Customer(first_name = "Matt", last_name = "Rosner", email = "rosboss@softball.com", company = "Softball Shop", phone_number = "123-523-9049", notes = "Mr. Rosner has some concern about the how the software integrates with his current technologies.", rep_id = 1)


# Commit customers to database
db.session.add_all([customer1,customer2, customer3, customer4, customer5, customer6])
db.session.commit()

# Create connections

conn1 = AdvRep(rep_id = 1, adv_id = 1)
conn2 = AdvRep(rep_id = 1, adv_id = 2)
conn3 = AdvRep(rep_id = 1, adv_id = 3)
conn4 = AdvRep(rep_id = 2, adv_id = 2)
conn5 = AdvRep(rep_id = 3, adv_id = 2)

db.session.add_all([conn1,conn2, conn3, conn4, conn5])
db.session.commit()

