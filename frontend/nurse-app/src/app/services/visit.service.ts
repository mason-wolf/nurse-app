import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Visit } from '../models/visit';

@Injectable({
  providedIn: 'root'
})
export class VisitService {

  constructor(private httpClient: HttpClient) { }

  getVisits() : Observable<Visit[]> {
    return this.httpClient.get<Visit[]>(environment.url + "/getVisits");
  }

  getWeek() {
    return this.httpClient.get(environment.url + "/getWeek");
  }

  scheduleVisit(visit: Visit) {
    return this.httpClient.post(environment.url + "/scheduleVisit", visit);
  }

  unscheduleVisit(visit_id) {
    return this.httpClient.post(environment.url + "/unscheduleVisit", visit_id);
  }

  getVisitsByPatient(patient_id): Observable<Visit[]> {
    return this.httpClient.post<Visit[]>(environment.url + "/getVisitsByPatient", patient_id);
  }
}
