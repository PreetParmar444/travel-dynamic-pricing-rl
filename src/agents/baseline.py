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