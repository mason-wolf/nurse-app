import { Component, OnInit, TemplateRef, ViewChild } from '@angular/core';
import { PatientService } from '../services/patient.service';
import { VisitService } from '../services/visit.service';
import { MatDialog } from '@angular/material/dialog';
import { Patient } from '../models/patient';
import { Visit } from '../models/visit';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  week = [];
  @ViewChild('schedulePatientDialog') schedulePatientDialog = {} as TemplateRef<any>;
  @ViewChild('viewVisitDialog') viewVisitDialog = {} as TemplateRef<any>;

  searchTerm: string;
  selectedDate: string;
  selectedVisit: Visit;

  visits: Visit[] = [];
  patientSearch: Patient[] = [];
  mileage = 0;

  constructor(private patientService: PatientService,
    private visitService: VisitService,
    private dialog: MatDialog) { }

  ngOnInit(): void {
    this.getWeek();
  }

  getWeek() {
    this.week =  [];
    this.visits = [];
    this.mileage = 0;
    this.visitService.getWeek().subscribe(resp => {

      for (var day in resp) {
        let date = new Date(resp[day]["date"]);
        date.setHours(date.getHours() + 6);
        this.week.push(date);

        for (var visit in resp[day]["visits"]) {
          let date = new Date(resp[day]["visits"][visit]["date"]);
          date.setHours(date.getHours() + 6);
          resp[day]["visits"][visit]["date"] = date.toString();
          this.visits.push(resp[day]["visits"][visit]);
          let visit_mileage = resp[day]["visits"][visit];
          if (visit_mileage["mileage_exempt"] != true) {
            this.mileage += visit_mileage["mileage"];
          }
        }
      }
    });
  }

  getVisit(visit: Visit) {
    this.selectedVisit = visit;
    this.dialog.open(this.viewVisitDialog);
  }

  updateVisit() {
    this.visitService.updateVisit(this.selectedVisit).subscribe(value => {
      this.getWeek();
    });
  }

  unscheduleVisit() {
    this.visitService.unscheduleVisit(this.selectedVisit.id).subscribe(value => {
      this.selectedVisit = new Visit();
      this.getWeek();
    });
  }
  showSchedulePatient(date) {
    this.selectedDate = date;
    this.dialog.open(this.schedulePatientDialog);
  }

  searchPatient() {
    this.patientService.searchPatient(this.searchTerm).subscribe(value => {
      this.patientSearch = value;
    });
  }

  schedulePatient(patient: Patient) {
    let visit = new Visit();
    visit.patient_id = patient.id;
    visit.date = this.selectedDate;
    this.visits.push(visit);
    this.dialog.closeAll();
    this.visitService.scheduleVisit(visit).subscribe(value => {
      console.log(value);
      this.getWeek();
    });
  }
}
