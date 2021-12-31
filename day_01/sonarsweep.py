"""
Advent of Code 2021 Day 1: Sonar Sweep
"""

from pathlib import Path
from typing import List


def read_input_file(filename: Path = Path("day_01/input.txt")) -> List[int]:
    """
    Reads the input file and outputs the list of numbers that was in it.
    """
    sequence: List[int] = []
    with open(filename, 'r') as fd:
        for line in fd:
            sequence.append(int(line))
    return sequence


def generate_pairs(input_sequence: List[int]) -> List[List[int]]:
    """
    Takes the sequence input into it and returns the pairs for comparison.
    Example:
        Input: [1,2,3]
        Output: [[1,2],[2,3]]
    """
    out: List[List[int]] = []
    for i in range(1, len(input_sequence)):
        out.append([input_sequence[i-1], input_sequence[i]])
    return out


def generate_sliding_windows(input_sequence: List[int]) -> List[List[int]]:
    """
    Generates a sliding window of width three measurements for a given input sequence.
    """
    out: List[List[int]] = []
    for i in range(2, len(input_sequence)):
        out.append([input_sequence[i-2], input_sequence[i-1], input_sequence[i]])
    return out


def sum_inner_lists(input_lists: List[List[int]]) -> List[int]:
    """
    Takes a list of lists and returns a list of sums for those inner lists.
    Example:
        Input: [ [1,2], [2,3] ]
        Output:[ 3, 5 ]
    """
    out: List[int] = []
    for l in input_lists:
        out.append(sum(l))
    return out

def check_increases(input_pairs: List[List[int]]) -> List[bool]:
    """
    Checks if the second value of any given pair is greater than the first.
    """
    out: List[bool] = []
    for pair in input_pairs:
        if pair[1] > pair[0]:
            out.append(True)
        else:
            out.append(False)
    return out

if __name__ == "__main__":
    input_sequence = read_input_file()
    input_pairs = generate_pairs(input_sequence)
    print("Calculating regular increases:")
    increases = check_increases(input_pairs)
    increase_count = len([x for x in increases if x is True])
    print(f"Increases: {increase_count}")

    print("Calculating increases with sliding window:")
    sliding_windows = generate_sliding_windows(input_sequence)
    window_sums = sum_inner_lists(sliding_windows)
    window_pairs = generate_pairs(window_sums)
    increases = check_increases(window_pairs)
    increase_count = len([x for x in increases if x is True])
    print(f"Increases: {increase_count}")
