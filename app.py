from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return request.form['StartGame']
        #return render_template('Game.php')
    return render_template('index.php')
    

if __name__ == '__main__':
    app.run(debug=True)
