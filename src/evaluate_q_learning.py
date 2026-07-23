"""
Evaluate the trained Q-Learning agent against baseline strategies.
"""

import matplotlib.pyplot as plt

from src.env.pricing_env import DynamicPricingEnv
from src.agents.baseline import (
    FixedPriceAgent,
    TimeBasedDiscountAgent,
)
from src.agents.q_learning import QLearningAgent
from src.utils.evaluate import evaluate_agent


def evaluate_q_learning():
    """
    Evaluate Fixed Price, Time-Based Discount,
    and Trained Q-Learning agents.
    """

    env = DynamicPricingEnv()

    # -------------------------
    # Fixed Price Strategy
    # -------------------------
    fixed_agent = FixedPriceAgent(price_index=2)

    fixed_results = evaluate_agent(
        env,
        fixed_agent,
        episodes=200
    )

    # -------------------------
    # Time-Based Discount Strategy
    # -------------------------
    discount_agent = TimeBasedDiscountAgent()

    discount_results = evaluate_agent(
        env,
        discount_agent,
        episodes=200
    )

    # -------------------------
    # Trained Q-Learning Strategy
    # -------------------------
    q_agent = QLearningAgent()

    q_agent.load("models/q_table.npy")

    # Disable exploration during evaluation
    q_agent.epsilon = 0.0

    q_results = evaluate_agent(
        env,
        q_agent,
        episodes=200
    )

    return (
        fixed_results,
        discount_results,
        q_results,
    )


if __name__ == "__main__":

    fixed, discount, q_learning = evaluate_q_learning()

    print("\n==============================")
    print("Average Revenue Comparison")
    print("==============================")

    print(f"Fixed Price : {fixed['average_revenue']:.2f}")
    print(f"Discount    : {discount['average_revenue']:.2f}")
    print(f"Q-Learning  : {q_learning['average_revenue']:.2f}")

    # -------------------------
    # Bar Chart
    # -------------------------
    strategies = [
        "Fixed",
        "Discount",
        "Q-Learning",
    ]

    revenues = [
        fixed["average_revenue"],
        discount["average_revenue"],
        q_learning["average_revenue"],
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(strategies, revenues)

    plt.title("Average Revenue Comparison")
    plt.ylabel("Average Revenue")
    plt.grid(axis="y")

    plt.tight_layout()
    plt.show()

    # -------------------------
    # Revenue Distribution
    # -------------------------
    plt.figure(figsize=(10, 5))

    plt.hist(
        fixed["revenues"],
        bins=20,
        alpha=0.5,
        label="Fixed"
    )

    plt.hist(
        discount["revenues"],
        bins=20,
        alpha=0.5,
        label="Discount"
    )

    plt.hist(
        q_learning["revenues"],
        bins=20,
        alpha=0.5,
        label="Q-Learning"
    )

    plt.title("Revenue Distribution")
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.legend()

    plt.tight_layout()
    plt.show()