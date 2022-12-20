import db
from geopy.geocoders import Nominatim

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

def updatePatient(patient):
    patient_id = patient["id"]
    first_name = patient["first_name"]
    last_name = patient["last_name"]
    address = patient["address"]
    notes = patient["notes"]

    address = address
    geolocator = Nominatim(user_agent="my_request")
    location = geolocator.geocode(address)

    query = "UPDATE patient SET first_name=%s, last_name=%s, address=%s, latitude=%s, longitude=%s, notes=%s WHERE id=%s"
    conn = db.getConnection()
    cursor = conn.cursor()
    if location is None:
        cursor.execute(query, (first_name, last_name, address, 0, 0, notes, patient_id))
    else:
        cursor.execute(query, (first_name, last_name, address, location.latitude, location.longitude, notes, patient_id))
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