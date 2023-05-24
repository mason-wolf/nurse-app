import json
from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS
from datetime import timedelta, date
import patient_dao as patientdb
import visit_dao as visitdb

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return jsonify({ "status" : "online"})

# Patients
@app.route('/getPatients', methods=['GET'])
def getPatients():
    patients = patientdb.getPatients()
    return jsonify(patients)

@app.route('/getPatientById', methods=['POST'])
def getPatientById():
    patient = patientdb.getPatientById(json.loads(request.data))
    return jsonify(patient[0])
    
@app.route('/addPatient', methods=['POST'])
def addPatient():
    response = patientdb.addPatient(json.loads(request.data))
    return jsonify(response)

@app.route('/updatePatient', methods=['POST'])
def updatePatient():
    response = patientdb.updatePatient(json.loads(request.data))
    return jsonify(response)

@app.route("/deletePatient", methods=['POST'])
def deletePatient():
    response = patientdb.deletePatient(json.loads(request.data))
    return jsonify(response)

@app.route('/searchPatient', methods=['POST'])
def searchPatient():
    response = patientdb.searchPatient(json.loads(request.data))
    return jsonify(response)

# Visits

@app.route('/getVisits', methods=['GET'])
def getVisits():
    response = visitdb.getVisits()
    return jsonify(response)

@app.route('/updateVisit', methods=['POST'])
def updateVisit():
    visit = json.loads(request.data)
    if "status" not in visit:
        visit["status"] = "Pending"
    if "visit_time" not in visit:
        visit["visit_time"] = ""
    if "mileage" not in visit:
        visit["mileage"] = 0
    if "mileage_exempt" not in visit:
        visit["mileage_exempt"] = False
    response = visitdb.updateVisit(visit)
    return jsonify(response)

@app.route('/scheduleVisit', methods=['POST'])
def scheduleVisit():
    response = visitdb.scheduleVisit(json.loads(request.data))
    return jsonify(response)

@app.route('/unscheduleVisit', methods=['POST'])
def unscheduleVisit():
    response = visitdb.unscheduleVisit(json.loads(request.data))
    return jsonify(response)

@app.route('/getVisitsByPatient', methods=['POST'])
def getPatientsByVisit():
    response = visitdb.getVisitsByPatient(json.loads(request.data))
    return jsonify(response)

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

    visits = []
    for day in week:
        visits_by_date = visitdb.getVisitByDate(day)
        visits.append({"date" : day, "visits" : visits_by_date})

    return jsonify(visits)

if __name__ == '__main__':
    app.run(host="localhost", port=80)