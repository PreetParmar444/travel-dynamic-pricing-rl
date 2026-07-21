"""
Tabular Q-Learning agent for dynamic pricing.
"""

import numpy as np

from src.utils.config import PRICE_LEVELS


class QLearningAgent:
    """
    Tabular Q-Learning Agent for Dynamic Pricing.
    """

    def __init__(
        self,
        learning_rate=0.1,
        discount_factor=0.95,
        epsilon=1.0,
        epsilon_decay=0.995,
        epsilon_min=0.01,
    ):
        """
        Initialize the Q-Learning agent.
        """
        self.lr = learning_rate
        self.gamma = discount_factor

        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

        # Dictionary-based Q-table
        # Key: (inventory, days_left)
        # Value: Q-values for each pricing action
        self.q_table = {}

    def get_q_values(self, state):
        """
        Return Q-values for a given state.
        If the state is new, initialize its Q-values to zero.
        """
        state = tuple(state)

        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(PRICE_LEVELS))

        return self.q_table[state]

    def select_action(self, state):
        """
        Select an action using the epsilon-greedy strategy.
        """
        if np.random.random() < self.epsilon:
            # Exploration
            return np.random.randint(len(PRICE_LEVELS))

        # Exploitation
        q_values = self.get_q_values(state)
        return np.argmax(q_values)

    def update(
        self,
        state,
        action,
        reward,
        next_state,
        done,
    ):
        """
        Update the Q-value using the Bellman equation.
        """
        state = tuple(state)
        next_state = tuple(next_state)

        current_q = self.get_q_values(state)[action]
        next_q = np.max(self.get_q_values(next_state))

        target = reward

        if not done:
            target += self.gamma * next_q

        new_q = current_q + self.lr * (target - current_q)

        self.q_table[state][action] = new_q

    def decay_epsilon(self):
        """
        Decay epsilon after each training episode.
        """
        self.epsilon = max(
            self.epsilon_min,
            self.epsilon * self.epsilon_decay
        )

    def save(self, path):
        """
        Save the Q-table to disk.
        """
        np.save(path, self.q_table)

    def load(self, path):
        """
        Load a previously saved Q-table.
        """
        self.q_table = np.load(
            path,
            allow_pickle=True
        ).item()