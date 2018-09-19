from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin



# configuration settings
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e3ffcebd06e040d938eadb2aff6deb89'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
admin = Admin(app)

from fakeshop import routes
