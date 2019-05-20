from flask import Flask, request, render_template, session
import TestPing
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = '89923u8923fj23u'
	
@app.route('/')
@app.route('/home')
def home():
	return TestPing.pingInfo()
	
app.run()