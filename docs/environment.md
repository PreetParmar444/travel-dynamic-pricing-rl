# Dynamic Pricing Environment

## State

The environment state is represented as:

```
(remaining_inventory, remaining_days)
```

Example:

```
(72, 15)
```

---

## Action

The agent selects one of the following prices:

| Action | Price |
|--------|------:|
|0|80|
|1|100|
|2|120|
|3|140|
|4|160|

---

## Reward

If a booking occurs:

```
Reward = Selected Price
```

Otherwise:

```
Reward = 0
```

---

## Episode Termination

An episode ends when:

- All inventory has been sold.

or

- The booking horizon reaches zero.