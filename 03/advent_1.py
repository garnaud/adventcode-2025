from dataclasses import dataclass
import argparse


@dataclass
class Joltage:
    original_joltage: str
    tens: int
    units: int

def compute(original_joltage: str) -> Joltage:
    max_tens = "0"
    max_units = "0"
    for digit in original_joltage[:-1]:
        if digit > max_tens:
            max_tens = digit
            max_units="0"
        elif digit > max_units:
            max_units = digit

    if original_joltage[-1] > max_units:
        max_units = original_joltage[-1]

    return Joltage(original_joltage, int(max_tens), int(max_units))


def main(data_file: str) -> int:
    result = 0
    with open(data_file, "r") as f:
        for data in f:
            joltage = compute(data.strip())
            print(joltage)
            result = result + 10*joltage.tens+joltage.units
            print(result)

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent!")
    parser.add_argument("data", type=str, help="Data file")
    args = parser.parse_args()
    try:
        print(main(args.data))
    except Error as e:
        print(e)
