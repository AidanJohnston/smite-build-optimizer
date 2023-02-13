# builds.py
from typing import List

class Build:
    def __init__(self, god, items):
        self.god = god
        self.items = items
        self.chosen_items = []

    def add_items(self, items):
        self.chosen_items.extend(items)

    def optimize(self):
        remaining_power = self.god.power - sum(item.power for item in self.chosen_items)
        remaining_cost = self.god.cost - sum(item.cost for item in self.chosen_items)

        # Sort items by power-to-cost ratio in descending order
        sorted_items = sorted(self.items, key=lambda item: item.power / item.cost, reverse=True)

        # Add items to the build until we reach the maximum power and cost
        optimized_build = []
        for item in sorted_items:
            if item.power <= remaining_power and item.cost <= remaining_cost:
                optimized_build.append(item)
                remaining_power -= item.power
                remaining_cost -= item.cost
            if remaining_power == 0 and remaining_cost == 0:
                break

        return optimized_build
