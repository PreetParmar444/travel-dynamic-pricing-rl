# Travel & Hospitality - Reinforcement Learning for Dynamic Pricing

## Overview

This project develops a Reinforcement Learning (RL) based dynamic pricing system for travel and hospitality businesses such as airlines and hotels. The objective is to maximize total revenue by learning optimal pricing strategies throughout a finite booking season.

Unlike traditional rule-based pricing, the RL agent continuously interacts with a simulated booking environment and learns pricing policies that balance higher profits with inventory utilization.

---

## Business Problem

Businesses selling limited inventory over a fixed time period face two major challenges:

- Selling inventory too early at low prices.
- Leaving inventory unsold near departure.

This project formulates the pricing process as a Markov Decision Process (MDP), enabling an RL agent to optimize pricing decisions based on the remaining inventory and time until departure.

---

## Project Objectives

- Design a custom Gymnasium environment simulating booking behavior.
- Implement baseline pricing strategies.
- Train Q-Learning and Deep Q-Network (DQN) agents.
- Evaluate learned pricing policies against traditional methods.
- Visualize pricing behavior and revenue performance.

---

## Reinforcement Learning Formulation

The pricing problem is formulated as a Markov Decision Process (MDP):

- **State:** Remaining inventory and remaining days.
- **Action:** Select one of several discrete pricing levels.
- **Reward:** Revenue earned from successful bookings.
- **Objective:** Maximize cumulative revenue across an entire booking season.

## Tech Stack

- Python
- Gymnasium
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## Project Structure

```text
travel-dynamic-pricing-rl/
│
├── data/
├── models/
├── notebooks/
├── results/
├── src/
│   ├── agents/
│   ├── dashboard/
│   ├── env/
│   └── utils/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Project Progress

## Week 1 ✅ Environment Development

- ✔ Project initialization
- ✔ Markov Decision Process (MDP) formulation
- ✔ Configuration management
- ✔ Stochastic customer demand simulator
- ✔ Custom Gymnasium environment
- ✔ Environment validation

## Upcoming Work

### Week 2

- Baseline pricing strategies
- Q-Learning implementation
- Policy comparison

### Week 3

- Deep Q-Network (DQN)
- Experience Replay
- Epsilon-Greedy Exploration

### Week 4

- Policy evaluation
- Revenue comparison
- Business dashboard
- GitHub deployment