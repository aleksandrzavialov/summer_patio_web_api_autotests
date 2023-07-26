from dataclasses import dataclass
from selene.support.shared import browser
from selene import have


@dataclass()
class Order:
    amount: float = 0.0

    def calculate_amount(self, *args):
        total_sum = 0.0
        total_count = 0
        for dish in args:
            total_sum += dish.count * float(dish.price.split(' ')[0])
            total_count += dish.count
        return int(total_sum), total_count

    def check_amount(self, calculated):
        browser.element('.btn-cart-payment:nth-of-type(1)').should(have.text(str(calculated[0])))
        browser.element('.counter-text').should(have.text(str(calculated[1])))
        return self


