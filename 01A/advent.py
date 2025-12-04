import csv
from dataclasses import dataclass
import re
import argparse


@dataclass
class Rotation:
    direction: str
    clicks: int


def load_rows(data_file: str) -> list[Rotation]:
    rotations = []
    with open(data_file, "r") as data:
        reader = csv.DictReader(data, ["rotation"])
        for row in reader:
            result = re.search("^([R|L])(\\d+)", row["rotation"])
            if result is None:
                raise ValueError(f"Can't parse row: {row}")
            original_clicks = int(result.group(2))
            clicks = original_clicks - int(original_clicks / 100) * 100
            rotations.append(Rotation(result.group(1), clicks))

    return rotations


def rotate(current: int, rotation: Rotation) -> int:
    result = current
    if rotation.direction == "L":
        result = result - rotation.clicks
        if result < 0:
            result = result + 100
    elif rotation.direction == "R":
        result = result + rotation.clicks
        if result > 99:
            result = result - 100
    if result > 100:
        result = result - int(result / 100) * 100
    return result


def main(data_file: str, current: int):
    zero_count = 0 if current != 0 else 1
    for rotation in load_rows(data_file):
        current = rotate(current, rotation)
        if current == 0:
            zero_count = zero_count + 1
    print(f"Code is {zero_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent!")
    parser.add_argument("data", type=str, help="Data file")
    args = parser.parse_args()
    main(args.data, 50)
