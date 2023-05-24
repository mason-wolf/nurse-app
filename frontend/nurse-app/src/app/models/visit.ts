export class Visit {
    id: string;
    patient_id: string;
    date: string;
    notes: string;
    status: string;
    visit_time: string;
    mileage: number;
    mileage_exempt: boolean;

    constructor() {
      this.status = "Pending";
      this.mileage = 0;
      this.mileage_exempt = false;
    }
}
