class UserEntity:
    def __init__(
        self, 
        id: int,
        name: str,
        email: str,
        pssword: str,
        role: str
    )

    self.id = id
    self.name = name
    self.email = email
    self. password = password
    self.role = role

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email}, role={self.role})"