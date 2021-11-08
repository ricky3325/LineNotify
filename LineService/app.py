from flask import Flask, render_template, url_for, request
from .. import  AccessToken.app as 
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello！'

@app.route('/getCode', methods=['POST'])
def Do_editInfo():
    code = request.form["code"]
    state = request.form["state"]
    return code

app.run(host='0.0.0.0')
