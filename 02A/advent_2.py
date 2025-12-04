from dataclasses import dataclass

import argparse
import logging
import sys


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


def is_invalid(id: str) -> bool:
    id_length = len(id)

    for number_of_parts in range(2, id_length + 1):
        if id_length % number_of_parts == 0:
            # The id can be splitted to equal parts
            part_length = int(id_length / number_of_parts)

            first_part = id[:part_length]
            all_equals = False

            for other_part_index in range(1, number_of_parts):
                # We isolated first part, now we compare to other part of the id
                other_part = id[
                    part_length * other_part_index : part_length
                    * (other_part_index + 1)
                ]
                if first_part != other_part:
                    all_equals = False
                    break
                else:
                    all_equals = True
            if all_equals:
                return True

    return False


def is_invalid_with_set(id: str) -> bool:
    id_length = len(id)

    for number_of_parts in range(2, id_length + 1):
        if id_length % number_of_parts == 0:
            # The id can be splitted to equal parts
            part_length = int(id_length / number_of_parts)

            first_part = id[:part_length]
            all_different_parts = set({first_part})

            for other_part_index in range(1, number_of_parts):
                # We isolated first part, now we compare to other part of the id
                other_part = id[
                    part_length * other_part_index : part_length
                    * (other_part_index + 1)
                ]
                all_different_parts.add(other_part)
            if len(all_different_parts) == 1:
                return True

    return False


def main(data_file: str):
    sum_of_invalid_ids = 0
    for idrange in load(data_file):
        for id in range(idrange.min, (idrange.max + 1)):
            if is_invalid(str(id)):
                logger.debug(f"{id} is invalid")
                sum_of_invalid_ids = sum_of_invalid_ids + id
            else:
                logger.debug(f"{id} is valid")

    logger.info(f"Code is {sum_of_invalid_ids}")


def init_logger(is_verbose: bool) -> None:
    global logger
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if is_verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent!")
    parser.add_argument("data", type=str, help="Data file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Debug mode")
    args = parser.parse_args()

    init_logger(args.verbose)
    main(args.data)
