# Config setup
import os
import ConfigParser
# Fetch the config ini file & its subscription key
Config = ConfigParser.ConfigParser()
Config.read(os.path.dirname(os.path.abspath(__file__)) + '/config.ini')
print Config.sections()
ocpApimSubscriptionKey = Config.get('ApplicationSettings','Ocp-Apim-Subscription-Key')

# App setup
from flask import Flask
from pagesearch import simple_page
app = Flask(__name__)
app.register_blueprint(simple_page)
