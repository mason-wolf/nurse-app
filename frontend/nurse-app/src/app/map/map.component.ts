import { Component, OnInit } from '@angular/core';
import * as L from 'leaflet';
import { VisitService } from '../services/visit.service';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})

export class MapComponent implements OnInit {

  private map;
  private visits: any[] = [];

  constructor(private visitService: VisitService) { }

  private initMap(): void {
    this.map = L.map('map', {
      center: [ 33.20097493343204, -87.54411968949736 ],
      zoom: 13
    });

    const tiles = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18,
      minZoom: 3,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });

    tiles.addTo(this.map);

    this.visitService.getWeek().subscribe(week => {
      for (var day in week) {
        for (var visit in week[day]["visits"]) {
          this.visits.push(week[day]["visits"][visit])
         // console.log(week[day]["visits"][visit]);
        }
      }
      console.log(this.visits);
      for (var visit in this.visits) {
        console.log(this.visits[visit]);
        if (this.visits[visit]["latitude"] != null && this.visits[visit]["longitude"] != null) {
          var marker = L.marker([this.visits[visit]["latitude"], this.visits[visit]["longitude"]]).addTo(this.map);
          marker.bindPopup("<b>" +
          this.visits[visit]["first_name"] +
          " " +
          this.visits[visit]["last_name"] +
          "</b><br><a href='http://maps.google.com/?q=" +
          this.visits[visit]["address"] + "'  target='_blank'>" + this.visits[visit]["address"] + "</a>").openPopup();
        }
      }
    });
    this.map.flyTo([33.20097493343204, -87.54411968949736], 13);
  }

  ngOnInit(): void {

  }

  ngAfterViewInit(): void {
    this.initMap();
  }
}
