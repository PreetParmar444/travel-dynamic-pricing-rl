import numpy as np


def evaluate_agent(env, agent, episodes=100):
    """
    Evaluate an agent over multiple booking seasons.

    Parameters
    ----------
    env : Gym Environment

    agent : Pricing agent

    episodes : int

    Returns
    -------
    dict
    """

    revenues = []

    for _ in range(episodes):

        state, info = env.reset()

        terminated = False

        while not terminated:

            action = agent.select_action(state)

            state, reward, terminated, truncated, info = env.step(action)

        revenues.append(env.total_revenue)

    return {
        "average_revenue": np.mean(revenues),
        "max_revenue": np.max(revenues),
        "min_revenue": np.min(revenues),
        "std_revenue": np.std(revenues),
        "revenues": revenues
    }