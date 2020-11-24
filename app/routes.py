from flask import Flask, render_template
import serial

app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

@app.route('/')
@app.route('/index')
def index():
	ser.flush()
	if ser.in_waiting > 0:
		line = ser.readline().decode('utf-8').rstrip()
	else:
		line = 0
	return render_template('index.html', title='Home', user=line)

if __name__ == '__main__':
	app.run(debug=True, port=80, host='0.0.0.0')
