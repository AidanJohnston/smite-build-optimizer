# utils.py
import json

def load_gods_from_file(filename: str):
    with open(filename, "r") as f:
        gods = json.load(f)

    return [God(god["name"], god["power"], god["cost"]) for god in gods]

def load_items_from_file(filename: str):
    with open(filename, "r") as f:
        items = json.load(f)

    return [Item(item["name"], item["power"], item["cost"]) for item in items]

def save_build_to_file(build, filename):
    items = [{"name": item.name, "power": item.power, "cost": item.cost} for item in build]

    with open(filename, "w") as f:
        json.dump(items, f, indent=4)
