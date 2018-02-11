from flask import render_template
from ru_alumni import application
from flask import Flask, redirect, url_for, session, request, jsonify
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix
import os 
from ru_alumni import urls

#for SSL
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
#os.environ['LIN_CLIENT_KEY']= '78gbrnp4ovmhd3'
#os.environ['LIN_SECRET_KEY']= 'F8yif7Bjr86xKdAf'

# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.secret_key = os.urandom(24)

client_id = os.environ['LIN_CLIENT_KEY'];
client_secret = os.environ['LIN_SECRET_KEY'];

 # OAuth endpoints given in the LinkedIn API documentation
authorization_base_url = urls.OAUTH_BASE_URL
token_url = urls.TOKEN_URL
reg_redirect = urls.REDIRECT


@application.route("/authorize")
def login():
    linkedin = OAuth2Session(client_id, redirect_uri=reg_redirect)
    linkedin = linkedin_compliance_fix(linkedin)
    authorization_url, state = linkedin.authorization_url(authorization_base_url)
    session['oauth_state'] = state;
    return redirect(authorization_url);

@application.route("/login", methods=["GET"])
def callback():
    linkedin = OAuth2Session(client_id,redirect_uri=reg_redirect,state=session['oauth_state'])
    token = linkedin.fetch_token(token_url, client_secret=client_secret,authorization_response=request.url)  
    session['oauth_token'] = token
    return redirect(url_for('.profile'))

@application.route("/profile", methods=["GET"])
def profile():
    linkedin = OAuth2Session(client_id, redirect_uri=reg_redirect,token=session['oauth_token'])
    r = jsonify(linkedin.get(urls.USER_DATA).json())
    return r


@application.route('/')
def index():
    return render_template('index.html')

