import { Component, OnInit } from '@angular/core';
import { PatientService } from '../services/patient.service';
import { VisitService } from '../services/visit.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  week = [];

  constructor(private patientService: PatientService, private visitService: VisitService) { }

  ngOnInit(): void {
    this.visitService.getWeek().subscribe(resp => {
      for (var day in resp) {
        let date = new Date(resp[day]);
        date.setHours(date.getHours() + 6);
        this.week.push(date);
      }
    });
  }

}
