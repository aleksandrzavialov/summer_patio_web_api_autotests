from dataclasses import dataclass


@dataclass()
class Dish:
    name: str
    group: str
    mass: str
    price: str
    count: int = 0



