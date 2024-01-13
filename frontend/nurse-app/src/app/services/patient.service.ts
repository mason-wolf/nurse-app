import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Patient } from '../models/patient';
import { Observable } from 'rxjs/internal/Observable';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PatientService {

  constructor(private httpClient: HttpClient) { }

  getPatients(): Observable<Patient[]> {
    return this.httpClient.get<Patient[]>(environment.url + '/getPatients');
  }

  getPatientById(patient_id: string) : Observable<Patient> {
    return this.httpClient.post<Patient>(environment.url + "/getPatientById", patient_id);
  }

  addPatient(patient: Patient) {
    return this.httpClient.post(environment.url + "/addPatient", patient);
  }

  searchPatient(searchTerm: string): Observable<Patient[]> {
    return this.httpClient.post<Patient[]>(environment.url + "/searchPatient", {search_term: searchTerm})
  }

  updatePatient(patient: Patient) {
    return this.httpClient.post(environment.url + "/updatePatient", patient);
  }

  deletePatient(patient_id: string) {
    return this.httpClient.post(environment.url + "/deletePatient", patient_id);
  }

  searchPatientByNotes(searchTerm: string) {
    return this.httpClient.post<Patient[]>(environment.url + "/searchNotes", {search_term: searchTerm})
  }
}
