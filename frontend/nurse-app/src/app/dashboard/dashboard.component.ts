import { Component, OnInit } from '@angular/core';
import { PatientService } from '../services/patient.service';
import { VisitService } from '../services/visit.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(private patientService: PatientService, private visitService: VisitService) { }

  ngOnInit(): void {
    this.visitService.getWeek().subscribe(resp => {
      console.log(resp);
    });
  }

}
