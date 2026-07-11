"""
Configuration settings for the Dynamic Pricing RL environment.
"""

# Inventory settings
MAX_INVENTORY = 100

# Booking horizon (days until departure/check-in)
MAX_DAYS = 30

# Available pricing actions (in dollars or arbitrary units)
PRICE_LEVELS = [
    80,
    100,
    120,
    140,
    160
]

# Number of discrete actions
NUM_ACTIONS = len(PRICE_LEVELS)