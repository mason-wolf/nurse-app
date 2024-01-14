import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  email: string;
  password: string;
  error: string;

  constructor(private authService: AuthService, private router: Router) { }

  ngOnInit(): void {
  }

  login() {
    if (this.email != undefined && this.password != undefined) {
      this.authService.login(this.email, this.password).subscribe(res => {
        console.log(res);
        if(!res["error"]) {
          localStorage.setItem('access_token', res.access_token);
          sessionStorage.setItem('username', res.username);
          sessionStorage.setItem('userId', res.userId);
          this.router.navigate(['schedule']);
        }
        else {
          this.error = res;
        }
      });
    }
  }

}
