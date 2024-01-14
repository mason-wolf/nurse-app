import { Component, OnInit, TemplateRef, ViewChild, inject } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatTableDataSource } from '@angular/material/table';
import { ActivatedRoute, Router} from '@angular/router';
import { Patient } from '../models/patient';
import { Visit } from '../models/visit';
import { PatientService } from '../services/patient.service';
import { VisitService } from '../services/visit.service';
import {COMMA, ENTER} from '@angular/cdk/keycodes';
import { MatChipInputEvent } from '@angular/material/chips';

export interface Condition {
  name: string;
}


@Component({
  selector: 'app-patient-profile',
  templateUrl: './patient-profile.component.html',
  styleUrls: ['./patient-profile.component.css']
})

export class PatientProfileComponent implements OnInit {

  patient: Patient;

  recentVisits: MatTableDataSource<Visit>;
  displayedColumns : string[] = ["visit_id", "date", "notes"];

  visible = true;
  selectable = true;
  removable = true;
  addOnBlur = true;
  readonly separatorKeysCodes: number[] = [ENTER, COMMA];
  conditions: Condition[] = [];

  add(event: MatChipInputEvent): void {
    const input = event.input;
    const value = event.value;

    if ((value || '').trim()) {
      this.conditions.push({name: value.trim()});
    }
    if (input) {
      input.value = '';
    }
    if (value.trim() != "") {
      this.addCondition(value.trim())
    }
  }

  remove(condition: Condition): void {
    const index = this.conditions.indexOf(condition);

    if (index >= 0) {
      this.conditions.splice(index, 1);
    }
    let patientId = this.activatedRoute.snapshot.paramMap.get('patient_id');
    this.patientService.deletePatientCondition(patientId, condition.name).subscribe(value => {
   //   console.log(value);
    });
  }

  @ViewChild('updatePatientDialog') updatePatientDialog = {} as TemplateRef<any>;
  @ViewChild('deletePatientDialog') deletePatientDialog = {} as TemplateRef<any>;

  constructor(private activatedRoute: ActivatedRoute, private patientService: PatientService,
    private visitService: VisitService, private dialog: MatDialog, private route: Router) { }

  ngOnInit(): void {
    let patientId = this.activatedRoute.snapshot.paramMap.get('patient_id');
    this.patientService.getPatientById(patientId).subscribe(value => {
      this.patient = value;
    });

    this.visitService.getPatientVisits(patientId).subscribe(value => {
      this.recentVisits = new MatTableDataSource(value);
    })

    this.patientService.getPatientConditions(patientId).subscribe(value => {
      for (var c in value) {
        this.conditions.push({name: value[c]["condition_name"]});
      }
      // this.conditions.push({name: value.trim()});
    })
  }

  showUpdatePatient() {
    this.dialog.open(this.updatePatientDialog);
  }

  showDeletePatient() {
    this.dialog.open(this.deletePatientDialog);
  }

  addCondition(condition) {
    this.patientService.addPatientCondition(this.patient.id, condition).subscribe(value => {
      console.log(value);
    })
  }

  updatePatient() {
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
