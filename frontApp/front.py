## Front Page

from flask import Flask,render_template
import serial

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return  render_template('index.html', title='Home')

if __name__ == '__main__':
	app.run(debug=True, port=4000, host='127.0.0.1')
