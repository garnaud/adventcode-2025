from dataclasses import dataclass
import argparse
import traceback


def compute(original_joltage: str, number_of_batteries:int) -> int:
    max = 0 # initialize max digit
    position=0 # position of max digit in the input

    # take substring by removing last digits necessary for next iterations
    # number_of_batteries=5, the string "123456789", next iteration we need, at least, 4 digits, so we remove "6789" and search max on "12345".
    # So new list is current_list[:-4]; so current_list[:-(number_of_batteries-1)].
    # Special case: number_of_batteries=0 -> don't need to crop
    cropped_list = original_joltage[:-(number_of_batteries-1)] if number_of_batteries > 1 else original_joltage
    for index,digit in enumerate(cropped_list):
        # search the max in the cropped list
        digit = int(digit)
        if digit > max:
            max = digit
            # postition is helpful for next iteration
            position = index
    
    if number_of_batteries > 1:
        # For digit 'number_of_batteries', for instance, we will need to add (number_of_batteries-1) last digits, so we add this number of 0
        first = int(10 ** (number_of_batteries-1)) * max
        result = first + compute(original_joltage[(position+1):], number_of_batteries-1)
        return result
    
    return max

def main(data_file: str) -> int:
    result = 0
    with open(data_file, "r") as f:
        for data in f:
            joltage = compute(data.strip(),12)
            result = result + joltage

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent!")
    parser.add_argument("data", type=str, help="Data file")
    args = parser.parse_args()
    try:
        print(main(args.data))
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        
