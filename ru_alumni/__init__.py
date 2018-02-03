from flask import Flask
from flask_mail import Mail

application = Flask(__name__)
mail = Mail(application)

from ru_alumni import views
