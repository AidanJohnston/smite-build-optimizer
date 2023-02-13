import argparse

from gods import God
from items import Item
from builds import Build
from utils import load_gods_from_file, load_items_from_file, save_build_to_file

def parse_args():
    parser = argparse.ArgumentParser(description="Smite build optimizer")
    parser.add_argument("god", help="Name of the god to optimize build for")
    parser.add_argument("--gods-file", default="gods.json", help="File containing god data")
    parser.add_argument("--items-file", default="items.json", help="File containing item data")
    parser.add_argument("--output-file", default="build.json", help="File to save optimized build to")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    gods = load_gods_from_file(args.gods_file)
    god = next((god for god in gods if god.name == args.god), None)
    if not god:
        print(f"Error: Could not find god '{args.god}'")
        exit(1)

    items = load_items_from_file(args.items_file)

    build = Build(god, items)
    optimized_build = build.optimize()

    save_build_to_file(optimized_build, args.output_file)
