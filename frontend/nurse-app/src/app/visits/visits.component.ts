import { Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Visit } from '../models/visit';
import { VisitService } from '../services/visit.service';

@Component({
  selector: 'app-visits',
  templateUrl: './visits.component.html',
  styleUrls: ['./visits.component.css']
})
export class VisitsComponent implements OnInit {

  visits: MatTableDataSource<Visit>;
  displayedColumns : string[] = ["date", "last_name", "first_name"];
  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(private visitService: VisitService) { }

  ngOnInit(): void {
    this.visitService.getVisits().subscribe(value => {
      this.visits = new MatTableDataSource(value);
      this.visits.paginator = this.paginator;
      this.visits.sort = this.sort;
    })
  }

}
