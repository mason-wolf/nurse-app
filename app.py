from flask import Flask
from flask.json import jsonify
from flask_cors import CORS
from datetime import datetime, timedelta, date

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return jsonify({ "status" : "online"})

@app.route('/getWeek')
def get_week():
    week = []

    today = date.today()
    sunday = (today.weekday() - 6) % 7
    saturday = (today.weekday() - 4) % 7

    last_sunday = today - timedelta(days=sunday)
    next_saturday = today + timedelta(days=saturday)

    start_date = date(last_sunday.year, last_sunday.month, last_sunday.day)
    end_date = date(next_saturday.year, next_saturday.month, next_saturday.day)

    delta = end_date - start_date 

    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i, hours=5)
        if(day.strftime("%A") != "Sunday" and day.strftime("%A") != "Saturday"):
            week.append(day)

    return jsonify(week)

if __name__ == '__main__':
    app.run(host="localhost", port=80)
    