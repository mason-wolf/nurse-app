import { Component, OnInit, TemplateRef, ViewChild } from '@angular/core';
import { PatientService } from '../services/patient.service';
import { VisitService } from '../services/visit.service';
import { MatDialog } from '@angular/material/dialog';
import { Patient } from '../models/patient';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  week = [];
  @ViewChild('schedulePatientDialog') schedulePatientDialog = {} as TemplateRef<any>;
  @ViewChild('addPatientDialog') addPatientDialog = {} as TemplateRef<any>;
  
  newPatient = new Patient();
  
  constructor(private patientService: PatientService, 
    private visitService: VisitService,
    private dialog: MatDialog) { }

  ngOnInit(): void {
    this.visitService.getWeek().subscribe(resp => {
      for (var day in resp) {
        let date = new Date(resp[day]);
        date.setHours(date.getHours() + 6);
        this.week.push(date);
      }
    });
  }

  showSchedulePatient() {
    this.dialog.open(this.schedulePatientDialog);
  }

  showAddPatient() {
    this.dialog.open(this.addPatientDialog);
  }

  addPatient() {
    console.log(this.newPatient);
  }

}
