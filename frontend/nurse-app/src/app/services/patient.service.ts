import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Patient } from '../models/patient';
import { Observable } from 'rxjs/internal/Observable';

@Injectable({
  providedIn: 'root'
})
export class PatientService {

  constructor(private httpClient: HttpClient) { }
  api = "http://localhost:80/"

  getPatients(): Observable<Patient[]> {
    return this.httpClient.get<Patient[]>(this.api + 'getPatients');
  }

  getPatientById(patient_id: string) : Observable<Patient> {
    return this.httpClient.post<Patient>(this.api + "getPatientById", patient_id);
  }

  addPatient(patient: Patient) {
    return this.httpClient.post(this.api + "addPatient", patient);
  }

  searchPatient(searchTerm: string): Observable<Patient[]> {
    return this.httpClient.post<Patient[]>(this.api + "searchPatient", {search_term: searchTerm})
  }

  updatePatient(patient: Patient) {
    return this.httpClient.post(this.api + "updatePatient", patient);
  }

  deletePatient(patient_id: string) {
    return this.httpClient.post(this.api + "deletePatient", patient_id);
  }
}
