from flask import render_template
from ru_alumni import application as app


@app.route('/')
def index():
    return render_template('index.html')
