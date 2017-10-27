from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE = 'postgresql://postgres:asd123@localhost/bookdb'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE
db = SQLAlchemy(app)



class Book(db.Model):
	__tablename__ = 'book'
	
	title = db.Column(db.String(80), nullable = False)
	id = db.Column(db.Integer, primary_key = True)

db.drop_all()
db.create_all()

# try to run this file:
# python database_setup.py
# you may receive the following error:
# ImportError: No module named 'psycopg2'
# This indicates that you need to install 'psycopg2' module
# which is the database adapter for SQLAlchmey
# To install the 'psycopg2' module:
# pip install psycopg2

