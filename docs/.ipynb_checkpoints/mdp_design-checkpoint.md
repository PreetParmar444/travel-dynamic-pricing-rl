# Markov Decision Process (MDP)

## Objective

Maximize total revenue over a finite booking season.

---

## State

The environment state consists of:

State = (Remaining Inventory, Remaining Days)

Example:

(75, 18)

Meaning:

- 75 seats/rooms remaining
- 18 days until departure

---

## Actions

The agent selects one pricing level from:

| Action | Price |
|--------|------:|
| 0 | 80 |
| 1 | 100 |
| 2 | 120 |
| 3 | 140 |
| 4 | 160 |

---

## Reward

If a booking occurs:

Reward = Selected Price

Otherwise:

Reward = 0

---

## Episode Ends

The booking season terminates when:

- Inventory reaches zero

OR

- Remaining days become zero

---

## Transition

Each action influences the probability of receiving a booking.

Higher prices generally decrease demand.

Lower prices generally increase demand.

Remaining inventory and remaining days are updated after every step.