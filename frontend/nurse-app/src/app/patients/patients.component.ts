import { Component, OnInit, TemplateRef, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Patient } from '../models/patient';
import { PatientService } from '../services/patient.service';

@Component({
  selector: 'app-patients',
  templateUrl: './patients.component.html',
  styleUrls: ['./patients.component.css']
})
export class PatientsComponent implements OnInit {

  newPatient = new Patient();
  @ViewChild('addPatientDialog') addPatientDialog = {} as TemplateRef<any>;

  patients: MatTableDataSource<Patient>;
  displayedColumns : string[] = ["id", "last_name", "first_name"];
  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(private dialog: MatDialog, private patientService: PatientService) { }

  ngOnInit(): void {
    this.getPatients();
  }

  getPatients() {
    this.patientService.getPatients().subscribe(value => {
      this.patients = new MatTableDataSource(value);
      this.patients.paginator = this.paginator;
      this.patients.sort = this.sort;
    });
  }

  showAddPatient() {
    this.dialog.open(this.addPatientDialog);
  }

  addPatient() {
    this.patientService.addPatient(this.newPatient).subscribe(value => {
      this.newPatient = new Patient();
      this.getPatients();
    });
  }

}
