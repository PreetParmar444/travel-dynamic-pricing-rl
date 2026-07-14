"""
Custom Gymnasium environment for Dynamic Pricing.
"""

import gymnasium as gym
from gymnasium import spaces
import numpy as np

from src.utils.config import (
    MAX_INVENTORY,
    MAX_DAYS,
    PRICE_LEVELS,
)

from src.env.demand import simulate_customer_purchase


class DynamicPricingEnv(gym.Env):
    """
    Dynamic Pricing Environment for Reinforcement Learning.
    """

    metadata = {"render_modes": ["human"]}

    def __init__(self):
        super().__init__()

        self.max_inventory = MAX_INVENTORY
        self.max_days = MAX_DAYS

        # Action space: choose one of the available price levels
        self.action_space = spaces.Discrete(len(PRICE_LEVELS))

        # Observation space: [remaining_inventory, days_left]
        self.observation_space = spaces.Box(
            low=np.array([0, 0]),
            high=np.array([MAX_INVENTORY, MAX_DAYS]),
            dtype=np.int32,
        )

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.inventory = self.max_inventory
        self.days_left = self.max_days
        self.total_revenue = 0

        state = np.array(
            [self.inventory, self.days_left],
            dtype=np.int32,
        )

        return state, {}

    def step(self, action):
        price = PRICE_LEVELS[action]

        sale = False
        reward = 0

        if self.inventory > 0:
            sale = simulate_customer_purchase(
                price,
                self.days_left,
            )

        if sale:
            self.inventory -= 1
            reward = price
            self.total_revenue += reward

        self.days_left -= 1

        terminated = (
            self.inventory == 0
            or self.days_left == 0
        )

        truncated = False

        state = np.array(
            [self.inventory, self.days_left],
            dtype=np.int32,
        )

        info = {
            "price": price,
            "sale": sale,
            "revenue": self.total_revenue,
        }

        return (
            state,
            reward,
            terminated,
            truncated,
            info,
        )

    def render(self):
        print(
            f"Days Left: {self.days_left} | "
            f"Inventory: {self.inventory} | "
            f"Revenue: {self.total_revenue}"
        )