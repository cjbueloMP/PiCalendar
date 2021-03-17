from flask import render_template
from app import app
from .get_events import *

@app.route('/')
@app.route('/index')
def index():
    events = get_events()
    return render_template('index.html',events=events)
