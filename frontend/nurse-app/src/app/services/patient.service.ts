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
    return this.httpClient.get<Patient[]>(environment.url + '/patients/all');
  }

  getPatientById(patient_id: string) : Observable<Patient> {
    return this.httpClient.get<Patient>(environment.url + "/patients/" + patient_id);
  }

  addPatient(patient: Patient) {
    return this.httpClient.post(environment.url + "/patients", patient);
  }

  addPatientCondition(patient_id:string, condition: string) {
    return this.httpClient.post(environment.url + "/patients/conditions", { patient_id: patient_id, condition: condition})
  }

  getPatientConditions(patient_id: string) {
    return this.httpClient.get(environment.url + "/patients/" + patient_id + "/conditions");
  }

  deletePatientCondition(patient_id: string, condition_name: string) {
    return this.httpClient.delete(environment.url + "/patients/" + patient_id + "/conditions",
    { params: {condition_name: condition_name}})
  }

  searchPatientsByCondition(condition_name: string): Observable<any> {
    const url = `${environment.url}/patients/conditions/search?condition_name=${condition_name}`;
    return this.httpClient.get(url);
  }

  searchPatient(last_name: string): Observable<any> {
    const url = `${environment.url}/patients/search?last_name=${last_name}`;
    return this.httpClient.get(url);
  }

  updatePatient(patient: Patient) {
    return this.httpClient.put(environment.url + "/patients", patient);
  }

  deletePatient(patient_id: string) {
    return this.httpClient.delete(environment.url + "/patients/" + patient_id);
  }

  searchPatientByNotes(search_term: string) {
    const url = `${environment.url}/patients/notes/search?search_term=${search_term}`;
    return this.httpClient.get(url);
  }
}
