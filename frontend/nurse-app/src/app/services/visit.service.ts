import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class VisitService {

  constructor(private httpClient: HttpClient) { }

  getWeek() {
    return this.httpClient.get(environment.url + "/getWeek");
  }
}
