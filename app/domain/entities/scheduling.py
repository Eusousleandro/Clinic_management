import datetime


class Scheduling:
    def __init__(self, id, patient_id, provider_id, date, time):
        self.id = id
        self.patient_id = patient_id
        self.provider_id = provider_id
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        self.time = datetime.datetime.strptime(time, "%H:%M").time()

    def __str__(self):
        return f"Scheduling(id={self.id}, patient_id={self.patient_id}, provider_id={self.provider_id}, date={self.date}, time={self.time})"
    