import { Component, OnInit, TemplateRef, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatTableDataSource } from '@angular/material/table';
import { ActivatedRoute, Router} from '@angular/router';
import { Patient } from '../models/patient';
import { Visit } from '../models/visit';
import { PatientService } from '../services/patient.service';
import { VisitService } from '../services/visit.service';

@Component({
  selector: 'app-patient-profile',
  templateUrl: './patient-profile.component.html',
  styleUrls: ['./patient-profile.component.css']
})
export class PatientProfileComponent implements OnInit {

  patient: Patient;

  recentVisits: MatTableDataSource<Visit>;
  displayedColumns : string[] = ["visit_id", "date", "notes"];

  @ViewChild('updatePatientDialog') updatePatientDialog = {} as TemplateRef<any>;
  @ViewChild('deletePatientDialog') deletePatientDialog = {} as TemplateRef<any>;

  constructor(private activatedRoute: ActivatedRoute, private patientService: PatientService,
    private visitService: VisitService, private dialog: MatDialog, private route: Router) { }

  ngOnInit(): void {
    let patientId = this.activatedRoute.snapshot.paramMap.get('patient_id');
    this.patientService.getPatientById(patientId).subscribe(value => {
      this.patient = value;
    });

    this.visitService.getVisitsByPatient(patientId).subscribe(value => {
      this.recentVisits = new MatTableDataSource(value);
    })
  }

  showUpdatePatient() {
    this.dialog.open(this.updatePatientDialog);
  }

  showDeletePatient() {
    this.dialog.open(this.deletePatientDialog);
  }

  updatePatient() {
    console.log(this.patient);
    this.patientService.updatePatient(this.patient).subscribe(value => {
      console.log(value);
    });
  }

  deletePatient() {
    this.patientService.deletePatient(this.patient.id).subscribe(value => {
      console.log(value);
      this.route.navigate(["schedule"]);
    });
  }

}
