from flask import Blueprint, jsonify, request
import json
from flask_jwt_extended import jwt_required
from services import visit_service

visit_controller = Blueprint('visit_controller', __name__)

@visit_controller.route('/patients/visits', methods=['GET'])
@jwt_required()
def get_visits():
    response = visit_service.get_visits()
    return jsonify(response)


@visit_controller.route('/patients/visits', methods=['PUT'])
@jwt_required()
def update_visit():
    visit = json.loads(request.data)
    response = visit_service.update_visit(visit)
    return jsonify(response)


@visit_controller.route('/patients/visits', methods=['POST'])
@jwt_required()
def schedule_visit():
    response = visit_service.schedule_visit(json.loads(request.data))
    return jsonify(response)


@visit_controller.route('/patients/visits/<visit_id>', methods=['DELETE'])
@jwt_required()
def unschedule_visit(visit_id):
    response = visit_service.unschedule_visit(visit_id)
    return jsonify(response)


@visit_controller.route('/patients/<patient_id>/visits', methods=['GET'])
@jwt_required()
def get_visits_by_patient(patient_id):
    response = visit_service.get_visits_by_patient(patient_id)
    return jsonify(response)


@visit_controller.route('/week')
@jwt_required()
def get_week():
    return jsonify(visit_service.get_week())
