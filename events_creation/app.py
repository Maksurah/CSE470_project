app.py

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create_event', methods=['POST'])
def create_event():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    location = request.form['location']
    description = request.form['description']

    

    

if __name__ == '__main__':
    app.run(debug=True)
