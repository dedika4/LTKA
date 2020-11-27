## Application

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',title='Home')

if __name__ == '__main__':
	app.run(debug=True, port=5000, host='0.0.0.0')
