from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
	return render_template('index.html')

@app.route('/listdata')
def listeverything():

	req = request.args

	returnType = req.get("returnType", type=str)
	dataType = req.get("dataType", type=str)
	topVals = req.get("quantity", default = -1, type=int)
	
	r = requests.get(f'http://restapi:5000/{returnType}/{dataType}?top={topVals}')

	return r.text


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
