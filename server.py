"""Kredible server."""

from flask import Flask
from model import connect_to_db, db
from jinja2 import StrictUndefined
from crud import create_sales_adv, create_sales_rep

app = Flask(__name__)
app.secret_key= "gggc"
app.jinja_env.undefined = StrictUndefined





if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)