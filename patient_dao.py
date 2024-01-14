import db
from geopy.geocoders import Nominatim
import json 

def getPatients():
    query = "SELECT * FROM patient order by last_name asc"
    result = db.executeQuery(query, (''))
    return result

def getPatientById(patient_id):
    query = "SELECT * FROM patient WHERE id=%s"
    result = db.executeQuery(query, (patient_id,))
    return result
    
def addPatient(patient):
    first_name = patient["first_name"]
    last_name = patient["last_name"]
    address = patient["address"]
    notes = ""
    address = address
    geolocator = Nominatim(user_agent="my_request")
    location = geolocator.geocode(address)

    query = "INSERT INTO patient (first_name, last_name, address, latitude, longitude, notes) VALUES (%s, %s, %s, %s, %s, %s)"
    conn = db.getConnection()
    cursror = conn.cursor()

    if (location is None):
        cursror.execute(query, (first_name, last_name, address, 0, 0, notes))
    else:
        cursror.execute(query, (first_name, last_name, address, location.latitude, location.longitude, notes))
    conn.commit()
    cursror.close()
    conn.close()
    return {"response" : "patient_added"}

def searchPatient(search_term):
    patient = search_term["search_term"]
    query = "SELECT * FROM patient WHERE last_name LIKE %s"
    result = db.executeQuery(query, (patient,))
    return result

def searchPatientsByNote(search_term):
    searchTerm = search_term["search_term"]
    query = "SELECT * FROM patient WHERE notes LIKE " + "'%" + searchTerm.upper() + "%'"
    result = db.executeQuery(query, ())
    return result


def search_patients_by_condition(search_term):
    query = """
    SELECT p.first_name, p.last_name, p.id, p.notes, pc.condition_name
    FROM patient AS p
    INNER JOIN patient_conditions AS pc ON p.id = pc.patient_id
    WHERE pc.condition_name LIKE LOWER(%s) AND p.id IS NOT NULL
    """
    result = db.executeQuery(query, ('%' + search_term.lower() + '%',))
    return result

def add_patient_condition(patient_id, condition):
    query = "INSERT into patient_conditions (patient_id, condition_name) VALUES (%s, %s)"
    conn = db.getConnection()
    cursor = conn.cursor()
    cursor.execute(query, (patient_id, condition.upper()))
    conn.commit()
    cursor.close()
    conn.close()
    return {"response": "condition added"}


def get_patient_conditions(patient_id):
    query = "SELECT * FROM patient_conditions WHERE patient_id = %s"
    result = db.executeQuery(query, (patient_id,))
    return result

def delete_patient_condition(patient_id, condition):
    query = "DELETE FROM patient_conditions WHERE condition_name=%s AND patient_id = %s"
    conn = db.getConnection()
    cursor = conn.cursor()
    cursor.execute(query, (condition,patient_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"response" : "condition deleted"}

def updatePatient(patient):
    patient_id = patient["id"]
    first_name = patient["first_name"]
    last_name = patient["last_name"]
    address = patient["address"]
    notes = patient["notes"].upper()
    phone_number = patient["phone_number"]
    geolocator = Nominatim(user_agent="my_request")
    location = geolocator.geocode(address)
    query = "UPDATE patient SET first_name=%s, last_name=%s, notes=%s WHERE id=%s"
    conn = db.getConnection()
    cursor = conn.cursor()

    cursor.execute(query, (first_name, last_name, notes, patient_id))
      #  cursor.execute(query, (first_name, last_name, address, phone_number, location.latitude, location.longitude, notes, patient_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"response" : "patient_updated"}

def deletePatient(patient_id):
    query = "DELETE FROM patient WHERE id=%s"
    conn = db.getConnection()
    cursor = conn.cursor()
    cursor.execute(query, (patient_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"response" : "patient_deleted"}