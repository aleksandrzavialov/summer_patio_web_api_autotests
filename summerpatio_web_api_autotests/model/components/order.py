from dataclasses import dataclass


@dataclass()
class Order:
    amount: float = 0.0

    def calculate_amount(self, *args):
        total_sum = 0.0
        for dish in args:
            total_sum += dish.count * float(dish.price.split(' ')[0])
        return self
