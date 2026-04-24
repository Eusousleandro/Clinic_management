class ServiceEntity:
    def __init__(
            self, 
            name: str, 
            description: str,
            duration_minutes: int,
            price: float
        ):

        self.name = name
        self.description = description
        self.duration_minutes = duration_minutes
        self.price = price
