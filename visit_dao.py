from datetime import datetime
import db

def scheduleVisit(visit):
    patient_id = visit["patient_id"]
    date = visit["date"]
    date = date[:-14]
    query = "INSERT INTO visit (patient_id, date, status) VALUES (%s, %s, %s)"
    conn = db.getConnection()
    cursror = conn.cursor()
    cursror.execute(query, (patient_id, date, visit["status"]))
    conn.commit()
    cursror.close()
    conn.close()
    return {"response" : "visit_scheduled", "data" : visit}

def updateVisit(visit):
    query = "UPDATE visit SET status=%s, visit_time=%s, mileage=%s, mileage_exempt=%s, notes=%s WHERE id=%s"
    conn = db.getConnection()
    cursor = conn.cursor()
    cursor.execute(query, (visit["status"], visit["visit_time"], visit["mileage"], visit["mileage_exempt"], visit["notes"], visit["id"],))
    conn.commit()
    cursor.close()
    return { "status" : "visit_updated"}

def getVisits():
    query = "SELECT visit.id, visit.notes, date, address, first_name, last_name, patient_id FROM visit INNER JOIN patient on visit.patient_id=patient.id order by date desc"
    result = db.executeQuery(query, (''))
    return result
    
def getVisitByDate(date):
    query = "SELECT date, first_name, last_name, address, patient.id as patient_id, patient.latitude, patient.longitude, visit.id, visit.status, visit.visit_time, visit.notes, visit.mileage, visit.mileage_exempt FROM visit INNER JOIN patient ON visit.patient_id=patient.id WHERE date=%s"
    result = db.executeQuery(query, (date,))
    return result

def getVisitsByPatient(patient_id):
    query = "SELECT * FROM visit WHERE patient_id=%s order by date desc"
    result = db.executeQuery(query, (patient_id,))
    return result
    
def unscheduleVisit(visit_id):
    query = "DELETE FROM visit where id=%s"
    conn = db.getConnection()
    cursor = conn.cursor()
    cursor.execute(query, (visit_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"response" : "visit_unscheduled", "data" : visit_id}