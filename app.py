from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])

def calculate():
    birthdate = request.form['birthdate']
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    today = datetime.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (today.replace(month=today.month - 1, day=1) - today.replace(month=today.month, day=1)).days

    if months < 0:
        years -= 1
        months += 12

    return render_template('index.html', age=f"{years} years, {months} months, and {days} days")

if __name__ == '__main__':
    app.run(debug=True)
