from flask import render_template
from app import app
from app.data import positionData

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dewa Mahardika'}
    pos = positionData()
    pos.getDistance()
    pos.getDirection()
    return render_template('index.html', title='Home', user=user, data=pos)
