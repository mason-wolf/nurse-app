import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { PatientService } from '../services/patient.service';
import { Patient } from '../models/patient';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  patients: MatTableDataSource<Patient>;
  displayedColumns : string[] = ["id", "last_name", "first_name", "condition"];
  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(private route: ActivatedRoute, private patientService: PatientService) { }

  ngOnInit(): void {
    this.route.queryParamMap.subscribe(terms=> {
      this.patientService.searchPatientsByCondition(terms["params"].searchTerm).subscribe(value => {
        console.log(value)
        this.patients = new MatTableDataSource(value);
      })
    })
  }

}
