# Dynamic Pricing Workflow

```text
Customer Arrives
       │
       ▼
Current State
(Inventory, Days Left)
       │
       ▼
RL Agent Chooses Price
       │
       ▼
Demand Simulator
       │
       ▼
Booking?
   │        │
  Yes       No
   │        │
Reward=Price Reward=0
   │        │
   ▼        ▼
Update Inventory & Time
       │
       ▼
Next State
```