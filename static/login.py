from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def do():
    if request.form['Add Nickname']:
        name = request.form['NewNameField']
        addNewName(name)
        render_template('login.php')