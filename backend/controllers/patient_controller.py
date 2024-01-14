from flask import Blueprint, jsonify, request
import json
from flask_jwt_extended import jwt_required
from services import patient_service

patient_controller = Blueprint('patient_controller', __name__)


@patient_controller.route('/patients/all', methods=['GET'])
@jwt_required()
def get_patients():
    patients = patient_service.get_patients()
    return jsonify(patients)


@patient_controller.route('/patients/<patient_id>', methods=['GET'])
@jwt_required()
def get_patient_by_id(patient_id):
    patient = patient_service.get_patient_by_id(patient_id)
    return jsonify(patient)
    

@patient_controller.route('/patients', methods=['POST'])
@jwt_required()
def add_patient():
    response = patient_service.add_patient(json.loads(request.data))
    return jsonify(response)


@patient_controller.route('/patients', methods=['PUT'])
@jwt_required()
def update_patient():
    response = patient_service.update_patient(json.loads(request.data))
    return jsonify(response)


@patient_controller.route('/patients/conditions', methods=['POST'])
@jwt_required()
def add_patient_condition():
    payload = json.loads(request.data)
    response = patient_service.add_patient_condition(payload["patient_id"], 
                                                     payload["condition"])
    return jsonify(response)


@patient_controller.route('/patients/<patient_id>/conditions', 
                          methods=['GET'])
@jwt_required()
def get_patient_conditions(patient_id):
    response = patient_service.get_patient_conditions(patient_id)
    return jsonify(response)


@patient_controller.route('/patients/<patient_id>/conditions', 
                          methods=['DELETE'])
@jwt_required()
def delete_patient_condition(patient_id):
    condition_name = request.args.get('condition_name')
    response = patient_service.delete_patient_condition(patient_id,
                                                        condition_name)
    return jsonify(response)


@patient_controller.route('/patients/conditions/search', methods=['GET'])
@jwt_required()
def search_patients_by_condition():
    condition_name = request.args.get('condition_name')
    response = patient_service.search_patients_by_condition(
        condition_name.upper())
    return jsonify(response)


@patient_controller.route("/patients/<patient_id>", methods=['DELETE'])
@jwt_required()
def delete_patient(patient_id):
    response = patient_service.delete_patient(patient_id)
    return jsonify(response)


@patient_controller.route('/patients/search', methods=['GET'])
@jwt_required()
def search_patient():
    last_name = request.args.get('last_name')
    response = patient_service.search_patient(last_name.upper())
    return jsonify(response)


@patient_controller.route('/patients/notes/search', methods=['GET'])
@jwt_required()
def search_patients_by_notes():
    search_term = request.args.get('search_term')
    response = patient_service.search_patients_by_notes(
        search_term.upper())
    return jsonify(response)