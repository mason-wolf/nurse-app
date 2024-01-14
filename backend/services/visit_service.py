from datetime import date, timedelta
from repositories import visit_repository


def schedule_visit(visit):
    return visit_repository.schedule_visit(visit)


def get_week():
    week = []

    today = date.today()
    sunday = (today.weekday() - 6) % 7
    saturday = (today.weekday() - 4) % 7

    last_sunday = today - timedelta(days=sunday)
    next_saturday = today + timedelta(days=saturday)

    start_date = date(last_sunday.year, 
                      last_sunday.month, last_sunday.day)
    end_date = date(next_saturday.year, 
                    next_saturday.month, next_saturday.day)

    delta = end_date - start_date 

    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i, hours=5)
        if(day.strftime("%A") != "Sunday" and 
           day.strftime("%A") != "Saturday"):
            week.append(day)

    visits = []
    for day in week:
        visits_by_date = visit_repository.get_visit_by_date(day)
        visits.append({"date" : day, "visits" : visits_by_date})
    return visits


def get_visits_by_patient(patient_id):
    return visit_repository.get_visits_by_patient(patient_id)


def get_visits():
    return visit_repository.get_visits()


def update_visit(visit):
    if "status" not in visit:
        visit["status"] = "Pending"
    if "visit_time" not in visit:
        visit["visit_time"] = ""
    if "mileage" not in visit:
        visit["mileage"] = 0
    if "mileage_exempt" not in visit:
        visit["mileage_exempt"] = False
    return visit_repository.update_visit(visit)


def unschedule_visit(visit_id):
    return visit_repository.unschedule_visit(visit_id)