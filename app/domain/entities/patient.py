import datetime

class Patient:
    def __init__(
        self, 
        id,
        name,
        email,
        cpf,
        date_of_birth,
        sex,
        phone,
        address,
        city,
        state,
        code,
        observations,
        created_at,
        updated_at
    ): 
        self.id = id
        self.name = name
        self.email = email
        self.cpf = cpf
        self.date_of_birth date_of_birth
        self.sex = sex
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.code = code
        self.observations = observations
        self.created_at = datetime.datetime.striptime(created_at, "%Y-%m-%d").created_at()
        self.updated_at = datetime.datetime.striptime(updated_at, "%H:%M").updated_at()

    def __str__(self):
        return f"Patient(
        id={self.id}, name{self.name}, email={self.email}, cpf={self.cpf}, date_of_birth={self.date_of_birth}, sex={self.sex},
        phone={self.phone}, address={self.adress}, city={self.city}, state={self.state}, code={self.code}, observations={self.observations},
        created_at={self.created_at}, updated_at={self.updated_at})"