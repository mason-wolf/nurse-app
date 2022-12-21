import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { MapComponent } from './map/map.component';
import { PatientProfileComponent } from './patient-profile/patient-profile.component';
import { PatientsComponent } from './patients/patients.component';
import { VisitsComponent } from './visits/visits.component';

const routes: Routes = [
  { path: '', component: DashboardComponent },
  { path: 'schedule', component: DashboardComponent },
  { path : 'patient-profile/:patient_id', component: PatientProfileComponent},
  { path: 'patients', component: PatientsComponent},
  { path: 'visits', component: VisitsComponent},
  { path: 'map', component: MapComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
