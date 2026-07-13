"""
Demand simulation for the Dynamic Pricing environment.
"""

import numpy as np
from src.utils.config import PRICE_LEVELS


def calculate_purchase_probability(price: float, days_left: int, max_days: int = 30) -> float:
    """
    Calculate the probability that a customer purchases
    at a given price and remaining booking horizon.

    Parameters
    ----------
    price : float
        Current selling price.

    days_left : int
        Remaining days before departure.

    max_days : int
        Total booking horizon.

    Returns
    -------
    float
        Purchase probability between 0 and 1.
    """

    # Higher prices reduce demand
    price_factor = np.exp(-(price - min(PRICE_LEVELS)) / 80)

    # Demand increases as departure approaches
    urgency_factor = 1 + (max_days - days_left) / max_days

    probability = 0.45 * price_factor * urgency_factor

    return np.clip(probability, 0, 1)


def simulate_customer_purchase(price: float, days_left: int) -> bool:
    """
    Simulate whether a customer purchases.

    Returns
    -------
    bool
        True if purchase occurs.
    """

    purchase_probability = calculate_purchase_probability(price, days_left)

    return np.random.random() < purchase_probability