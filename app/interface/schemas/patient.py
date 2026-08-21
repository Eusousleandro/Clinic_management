from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str,
    email: str,
    cpf:str,
    date_of_birth: str,
    sex: str,
    phone: str,
    address: str,
    city: str,
    state: str,
    code: str,
    observations: str

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    name: str | None
    email: str | None
    cpf: str | None 
    date_of_birth: str | None
    sex: str | None
    phone: str | None 
    address: str | None
    city: str | None
    state: str | None
    code: str | None
    observations: str | None

class PatientResponse(BaseModel):
    id: int,
    name: str, 
    email: str,
    cpf: str,
    date_of_birth: str,
    sex: str,
    phone: str
    address: str
    city: str
    state: str
    code: str,
    observations: str