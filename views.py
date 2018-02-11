from flask import Flask, redirect, url_for, session, request, jsonify
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix
import os 
import keys

#for SSL
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.secret_key = os.urandom(24)

client_id = keys.LIN_CLIENT_KEY;
client_secret = keys.LIN_SECRET_KEY;

 # OAuth endpoints given in the LinkedIn API documentation
authorization_base_url = 'https://www.linkedin.com/uas/oauth2/authorization'
token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'
reg_redirect = 'http://ru-alumni.36sn3vntw3.us-east-2.elasticbeanstalk.com/login'

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))


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
    r = jsonify(linkedin.get('https://api.linkedin.com/v1/people/~:(id,first-name,last-name,email-address,headline,num-connections,industry,picture-url,location)?format=json').json())
    return r

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
#     application.debug = True
#     os.environ['DEBUG'] = '1'
    
    application.debug = True
    application.run()

