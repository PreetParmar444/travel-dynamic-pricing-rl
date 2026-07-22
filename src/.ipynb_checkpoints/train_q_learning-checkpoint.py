"""
Train a Q-Learning agent for the Dynamic Pricing environment.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from src.env.pricing_env import DynamicPricingEnv
from src.agents.q_learning import QLearningAgent


def train_q_learning(
    episodes=5000,
    save_path="models/q_table.npy"
):
    """
    Train a Q-Learning agent.

    Parameters
    ----------
    episodes : int
        Number of training episodes.

    save_path : str
        Path to save the trained Q-table.

    Returns
    -------
    agent : QLearningAgent
        Trained agent.

    episode_rewards : list
        Total reward obtained in each episode.
    """

    env = DynamicPricingEnv()
    agent = QLearningAgent()

    episode_rewards = []

    for episode in range(episodes):

        state, info = env.reset()

        done = False
        total_reward = 0

        while not done:

            # Select action
            action = agent.select_action(state)

            # Take action
            next_state, reward, terminated, truncated, info = env.step(action)

            done = terminated or truncated

            # Update Q-table
            agent.update(
                state,
                action,
                reward,
                next_state,
                done,
            )

            state = next_state
            total_reward += reward

        # Reduce exploration
        agent.decay_epsilon()

        episode_rewards.append(total_reward)

        if (episode + 1) % 500 == 0:
            print(
                f"Episode {episode + 1}/{episodes}"
                f" | Reward: {total_reward:.2f}"
                f" | Epsilon: {agent.epsilon:.3f}"
            )

    # Create models folder if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Save trained Q-table
    agent.save(save_path)

    print("\nTraining completed successfully.")
    print(f"Q-table saved to: {save_path}")

    return agent, episode_rewards


if __name__ == "__main__":

    # Train the agent
    agent, rewards = train_q_learning()

    # -------------------------------
    # Plot Episode Rewards
    # -------------------------------
    plt.figure(figsize=(10, 5))
    plt.plot(rewards)

    plt.title("Q-Learning Training Reward")
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # -------------------------------
    # Plot Moving Average Reward
    # -------------------------------
    window = 100

    if len(rewards) >= window:

        moving_avg = np.convolve(
            rewards,
            np.ones(window) / window,
            mode="valid"
        )

        plt.figure(figsize=(10, 5))
        plt.plot(moving_avg)

        plt.title("Moving Average Reward")
        plt.xlabel("Episode")
        plt.ylabel("Average Reward")
        plt.grid(True)
        plt.tight_layout()
        plt.show()