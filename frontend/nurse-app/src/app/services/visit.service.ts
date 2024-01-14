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
    return this.httpClient.get<Visit[]>(environment.url + "/patients/visits");
  }

  getWeek() {
    return this.httpClient.get(environment.url + "/week");
  }

  updateVisit(visit: Visit) {
    return this.httpClient.put(environment.url  + "/patients/visits", visit);
  }

  scheduleVisit(visit: Visit) {
    return this.httpClient.post(environment.url + "/patients/visits", visit);
  }

  unscheduleVisit(visit_id) {
    return this.httpClient.delete(environment.url + "/patients/visits/" + visit_id);
  }

  getPatientVisits(patient_id): Observable<Visit[]> {
    return this.httpClient.get<Visit[]>(environment.url + "/patients/" + patient_id + "/visits");
  }
}
