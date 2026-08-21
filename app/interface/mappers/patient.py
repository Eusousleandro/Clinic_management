from app.interface.schemas.patient import PatientResponse

def to_patient_response(patient: Patient) -> PatientResponse:
    return PatientResponse(
        id=patient.id,
        name=patient.name,
        email=patient.email,
        cpf=patient.cpf,
        date_of_birth=patient.date_of_birth,
        sex=patient.sex,
        phone=patient.phone,
        address=patient.address,
        city=patient.city,
        state=patient.state,
        code=patient.code,
        observations=patient.observations
    )