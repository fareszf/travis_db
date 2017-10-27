import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if os.environ.get('SQLALCHEMY_DATABASE_URI') is None:
	app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://postgres:asd123@localhost/bookdb'
else:	
	app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ['SQLALCHEMY_DATABASE_URI']
#The followoing command is to get rid of the following warning:
#C:\Python35-32\lib\site-packages\flask_sqlalchemy\__init__.py:839: FSADeprecatio
#nWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be d
#isabled by default in the future.  Set it to True or False to suppress this warn
#ing.
#  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

