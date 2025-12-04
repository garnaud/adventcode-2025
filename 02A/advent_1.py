import csv
from dataclasses import dataclass
import re
import argparse


@dataclass
class IdRange:
    min: int
    max: int


def load(data_file: str) -> list[IdRange]:
    ranges = []
    with open(data_file, "r") as f:
        data = f.readline()

    for range_str in data.split(","):
        ranges.append(
            IdRange(int(range_str.split("-")[0]), int(range_str.split("-")[1]))
        )
    return ranges


def is_invalid(id: int) -> bool:
    id_str = str(id)
    id_str_len = len(id_str)

    if id_str_len % 2 == 1:
        # Length odd can be invalid
        return False

    return id_str[: int(id_str_len / 2)] == id_str[int(id_str_len / 2) :]


def main(data_file: str):
    sum_of_invalid_ids = 0
    for idrange in load(data_file):
        for id in range(idrange.min, (idrange.max + 1)):
            if is_invalid(id):
                sum_of_invalid_ids = sum_of_invalid_ids + id

    print(f"Code is {sum_of_invalid_ids}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent!")
    parser.add_argument("data", type=str, help="Data file")
    args = parser.parse_args()
    main(args.data)
