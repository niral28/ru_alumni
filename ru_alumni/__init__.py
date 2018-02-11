from flask import Flask
from flask_mail import Mail

application = Flask(__name__)
application.config.from_object('ru_alumni.config.BaseConfig')

mail = Mail(application)

from ru_alumni import views
