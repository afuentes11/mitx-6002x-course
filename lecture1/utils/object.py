class Object:
    """
    Represents an object with a name, weight, and value.
    """

    def __init__(self, name: str, weight: int, value: int):
        self.name = name
        self.weight = weight
        self.value = value

    def get_value(self) -> int:
        return self.value

    def get_weight(self) -> int:
        return self.weight

    def __str__(self) -> str:
        return f"{self.name} <{self.value}, {self.weight}>"