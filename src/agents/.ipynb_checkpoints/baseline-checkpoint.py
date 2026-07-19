"""
Baseline pricing strategies.
"""

from src.utils.config import PRICE_LEVELS


class FixedPriceAgent:
    """
    Always selects the same price level.
    """

    def __init__(self, price_index: int = 2):
        self.price_index = price_index

    def select_action(self, state):
        """
        Returns the same pricing action
        regardless of the current state.
        """
        return self.price_index

    @property
    def price(self):
        return PRICE_LEVELS[self.price_index]
class TimeBasedDiscountAgent:
    """
    Decreases price as the departure date approaches.
    """

    def select_action(self, state):
        """
        Select a pricing action based on the remaining days.
        """

        inventory, days_left = state

        if days_left >= 25:
            return 4      # ₹160

        elif days_left >= 19:
            return 3      # ₹140

        elif days_left >= 13:
            return 2      # ₹120

        elif days_left >= 7:
            return 1      # ₹100

        else:
            return 0      # ₹80