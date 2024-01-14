import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})

export class AuthService {

  constructor(private httpClient : HttpClient, private router: Router) { }

  login(username: string, password: string) {
    this.logout();
    return this.httpClient.post<any>(environment.url + "/login", JSON.stringify({username, password}));
  }

  createaccount(username: string, password: string) {
    return this.httpClient.post(environment.url + "/users", JSON.stringify({username: username, password : password}));
  }

  logout() {
    let token = localStorage.removeItem('access_token');
    sessionStorage.removeItem('username');
    localStorage.removeItem('access_token');
    if (token == null) {
      this.router.navigate(['']);
    }
  }

  get isLoggedIn(): boolean {
    let authToken = localStorage.getItem('access_token');
    return (authToken !== null) ? true : false;
  }

  getToken() {
 //   console.log(localStorage.getItem('access_token'))
    return localStorage.getItem('access_token');
  }
}
