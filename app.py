import json
from flask import Flask, request, send_from_directory
from flask.json import jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from datetime import timedelta, date

import patient_dao as patientdb
import visit_dao as visitdb
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = "$2a$12$zONiXJp/wt6qRIf5H5ZMi.llhUnI95i4iwpV/FQljiL7gYxqdWVTm"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

# Handle Angular Routing
@app.route('/', defaults={'path': ''})
@app.route('/<string:path>')
@app.route('/<path:path>')
def static_proxy(path):
    if os.path.isfile('templates/' + path):
        return send_from_directory('templates', path)
    else:
        return send_from_directory("templates", "index.html")

class User():
    def __init__(self, email, password):
        self.id = 1
        self.email = email
        self.password = password

users = []
u1 = User("hannah.sanders1@calhoun.edu", "Stella2022")
u2 = User("mason", "test")
users.append(u1)
users.append(u2)

def load_user(email, password):
    for user in users:
        if user.email == email and user.password == password:
            return user

# Patients
@app.route('/getPatients', methods=['GET'])
@jwt_required()
def getPatients():
    patients = patientdb.getPatients()
    return jsonify(patients)

@app.route('/getPatientById', methods=['POST'])
@jwt_required()
def getPatientById():
    patient = patientdb.getPatientById(json.loads(request.data))
    return jsonify(patient[0])
    
@app.route('/addPatient', methods=['POST'])
@jwt_required()
def addPatient():
    response = patientdb.addPatient(json.loads(request.data))
    return jsonify(response)

@app.route('/updatePatient', methods=['POST'])
@jwt_required()
def updatePatient():
    response = patientdb.updatePatient(json.loads(request.data))
    return jsonify(response)

@app.route("/deletePatient", methods=['POST'])
@jwt_required()
def deletePatient():
    response = patientdb.deletePatient(json.loads(request.data))
    return jsonify(response)

@app.route('/searchPatient', methods=['POST'])
@jwt_required()
def searchPatient():
    response = patientdb.searchPatient(json.loads(request.data))
    return jsonify(response)

@app.route('/searchNotes', methods=['POST'])
@jwt_required()
def searchNotes():
    response = patientdb.searchPatientsByNote(json.loads(request.data))
    return jsonify(response)

# Visits
@app.route("/login", methods=['POST'])
def login():
    credentials = json.loads(request.data)
    print(credentials)
    user = User(credentials["username"], credentials["password"])
    login = load_user(user.email, user.password)
    if login is not None:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token, username=user.email, userId=user.id)
    else:
        return {"error": "403"}

@app.route('/getVisits', methods=['GET'])
@jwt_required()
def getVisits():
    response = visitdb.getVisits()
    return jsonify(response)

@app.route('/updateVisit', methods=['POST'])
@jwt_required()
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
@jwt_required()
def scheduleVisit():
    response = visitdb.scheduleVisit(json.loads(request.data))
    return jsonify(response)

@app.route('/unscheduleVisit', methods=['POST'])
@jwt_required()
def unscheduleVisit():
    response = visitdb.unscheduleVisit(json.loads(request.data))
    return jsonify(response)

@app.route('/getVisitsByPatient', methods=['POST'])
@jwt_required()
def getPatientsByVisit():
    response = visitdb.getVisitsByPatient(json.loads(request.data))
    return jsonify(response)

@app.route('/getWeek')
@jwt_required()
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
    app.run(host="0.0.0.0", debug=False, port=5000)