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

    this.visitService.getWeek().subscribe(value => {
      console.log(value);
    });
    
    var marker = L.marker([33.20097493343204, -87.54411968949736]).addTo(this.map);
    marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
    this.map.flyTo([33.20097493343204, -87.54411968949736], 13);
  }

  ngOnInit(): void {
  }

  ngAfterViewInit(): void {
    this.initMap();
  }
}
