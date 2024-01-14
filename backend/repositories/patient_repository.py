from models.patient import Patient
from repositories import db

def get_patients():
    query = "SELECT * FROM patient order by last_name asc"
    result = db.executeQuery(query, (''))
    return result


def get_patient_by_id(patient_id):
    query = "SELECT * FROM patient WHERE id=%s"
    result = db.executeQuery(query, (patient_id,))
    return result[0]


def add_patient(patient: Patient):
    query = """
    INSERT INTO patient 
    (first_name, last_name, address, latitude, longitude, notes) 
    VALUES (%s, %s, %s, %s, %s, %s)"""
    conn = db.getConnection()
    cursror = conn.cursor()

    if (patient.location is None):
        cursror.execute(query, (patient.first_name, patient.last_name, 
                                patient.address, 0, 0, patient.notes))
    else:
        cursror.execute(query, (patient.first_name, patient.last_name, 
                                patient.address, patient.location.latitude, 
                                patient.location.longitude, patient.notes))
    conn.commit()
    cursror.close()
    conn.close()
    return {"response" : "patient_added"}


def update_patient(patient: Patient):
    query = """UPDATE patient SET 
    first_name=%s, last_name=%s, phone_number=%s, notes=%s WHERE id=%s"""
    conn = db.getConnection()
    cursor = conn.cursor()

    cursor.execute(query, (
        patient.first_name, patient.last_name, patient.phone_number, 
        patient.notes, patient.patient_id))
      #  cursor.execute(query, (first_name, last_name, address, 
      #                         phone_number, location.latitude, 
      #                         location.longitude, notes, patient_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"response" : "patient_updated"}


def add_patient_condition(patient_id, condition):
    query = """INSERT into patient_conditions 
    (patient_id, condition_name) VALUES (%s, %s)"""
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
    query = """DELETE FROM patient_conditions 
    WHERE condition_name=%s AND patient_id = %s"""
    conn = db.getConnection()
    cursor = conn.cursor()
    cursor.execute(query, (condition,patient_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"response" : "condition deleted"}


def search_patients_by_condition(search_term):
    query = """
    SELECT p.first_name, p.last_name, p.id, p.notes, pc.condition_name
    FROM patient AS p
    INNER JOIN patient_conditions AS pc ON p.id = pc.patient_id
    WHERE pc.condition_name LIKE LOWER(%s) AND p.id IS NOT NULL
    """
    result = db.executeQuery(query, ('%' + search_term.lower() + '%',))
    return result


def delete_patient(patient_id):
    query = "DELETE FROM patient WHERE id=%s"
    conn = db.getConnection()
    cursor = conn.cursor()
    cursor.execute(query, (patient_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"response" : "patient_deleted"}


def search_patient(search_term):
    query = "SELECT * FROM patient WHERE last_name LIKE %s"
    result = db.executeQuery(query, (search_term,))
    return result


def search_patients_by_notes(search_term):
    query = """SELECT * FROM patient 
    WHERE notes LIKE LIKE LOWER(%s)"""
    result = db.executeQuery(query, (
        '%' + search_term.lower() + '%',))
    return result