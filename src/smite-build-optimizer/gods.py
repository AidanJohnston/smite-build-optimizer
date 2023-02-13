# gods.py
class God:
    def __init__(self, name, power, cost):
        self.name = name
        self.power = power
        self.cost = cost

    def __repr__(self):
        return f"God(name={self.name}, power={self.power}, cost={self.cost})"
