from models.patient import Patient
from repositories import patient_repository
from geopy.geocoders import Nominatim

def get_patients():
    return patient_repository.get_patients()


def get_patient_by_id(patient_id):
    return patient_repository.get_patient_by_id(patient_id)


def add_patient(patient):
    new_patient = Patient()
    new_patient.first_name = patient["first_name"]
    new_patient.last_name = patient["last_name"]
    new_patient.address = patient["address"]
    geolocator = Nominatim(user_agent="my_request")
    new_patient.location = geolocator.geocode(new_patient.address)
    return patient_repository.add_patient(new_patient)


def update_patient(patient):
    patient_updated = Patient()
    patient_updated.patient_id = patient["id"]
    patient_updated.first_name = patient["first_name"]
    patient_updated.last_name = patient["last_name"]
    patient_updated.address = patient["address"]
    patient_updated.notes = patient["notes"].upper()
    patient_updated.phone_number = patient["phone_number"]
    geolocator = Nominatim(user_agent="my_request")
    patient_updated.location = geolocator.geocode(patient_updated.address)
    return patient_repository.update_patient(patient_updated)


def add_patient_condition(patient_id, condition):
    return patient_repository.add_patient_condition(patient_id, condition)


def get_patient_conditions(patient_id):
    return patient_repository.get_patient_conditions(patient_id)


def delete_patient_condition(patient_id, condition):
    return patient_repository.delete_patient_condition(patient_id, condition)


def search_patients_by_condition(search_term):
    return patient_repository.search_patients_by_condition(search_term)


def delete_patient(patient_id):
    return patient_repository.delete_patient(patient_id)


def search_patient(search_term):
    return patient_repository.search_patient(search_term)


def search_patients_by_notes(search_term):
    return patient_repository.search_patients_by_notes(search_term)