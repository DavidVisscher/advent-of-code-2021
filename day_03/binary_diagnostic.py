"""
Advent of Code 2021 Day 3: Binary Diagnostic
"""
import copy
from typing import List, Dict
from attrs import define, validators, field, Factory


def parse_row(row_string: str):
    """
    Parses a single row string into a list of bools.
    Example:
        Input: "101010"
        Output: [True, False, True, False, True, False]
    """
    out = []
    for char in row_string:
        if char not in ["1", "0"]:
            raise ValueError(f"Invalid character in input: {char}, expected 1 or 0")

        if char == "1":
            out.append(True)
        if char == "0":
            out.append(False)
    return out


@define
class DiagnosticReport:
    binary_data: List[List[bool]] = field(validator=validators.instance_of(list), default=Factory(list))
    width: int = field(validator=validators.instance_of(int), default=0)

    @binary_data.validator
    def ensure_data_is_of_equal_width(self, attribute, value: List[List[bool]]):
        for row in value:
            # Make sure the row is a list
            if not isinstance(row, list):
                raise ValueError(f"Expected row of type list, got{type(row)}")
            # Save the first observed width value
            if self.width == 0:
                self.width = len(row)
                continue
            # Make sure each subsequent width is the same
            if len(row) != self.width:
                raise ValueError(f"Width of row in binary data is incorrect:\nGot {len(row)} Expected {self.width}")

    @classmethod
    def from_str(cls, input_string):
        report = cls()
        report.append_multiline(input_string)
        return report

    def append_multiline(self, input_str: str):
        for line in input_str.splitlines():
            self.append_line(line)

    def append_line(self, row_string: str):
        self.append_row(parse_row(row_string))

    def append_row(self, row: List[bool]):
        if self.width == 0:
            self.width = len(row)
        if len(row) != self.width:
            raise ValueError(f"Width of row is incorrect:\nGot {len(row)} Expected {self.width}")
        self.binary_data.append(row)

    @property
    def digit_counts(self):
        return self.count_digits(self.binary_data, self.width)

    @staticmethod
    def count_digits(binary_data: List[List[bool]], width: int):
        counts = []
        # Establish counters per row
        for _ in range(width):
            counts.append({True: 0, False: 0})

        # Count the rows
        for row in binary_data:
            for i in range(width):
                counts[i][row[i]] += 1

        return counts

    @property
    def gamma_rate(self):
        digits = ""
        for count in self.digit_counts:
            if count[True] > count[False]:
                digits += "1"
            else:
                digits += "0"

        return int(digits, 2)

    @property
    def epsilon_rate(self):
        digits = ""
        for count in self.digit_counts:
            if count[True] < count[False]:
                digits += "1"
            else:
                digits += "0"
        return int(digits, 2)

    @property
    def power_consumption(self):
        return self.gamma_rate * self.epsilon_rate

    @property
    def most_common_digits(self):
        return self.calculate_most_common_digits(self.binary_data)

    def calculate_most_common_digits(self, binary_data: List[List[bool]]) -> List[bool]:
        """
        Returns the most common digits for each column

        Values are memoized.
        """
        out = []

        for count in self.count_digits(binary_data, self.width):
            if count[True] >= count[False]:
                out.append(True)
            else:
                out.append(False)

        return out

    @property
    def least_common_digits(self):
        return self.calculate_least_common_digits(self.binary_data)

    def calculate_least_common_digits(self, binary_data: List[List[bool]]) -> List[bool]:
        """
        Determines the least common digits for each column.
        Inverse of most_common_digits
        """
        out = []
        for digit in self.calculate_most_common_digits(binary_data):
            out.append(not digit)
        return out

    @staticmethod
    def bool_list_to_str(bool_list: List[bool]) -> str:
        digits = ""
        for bin_digit in bool_list:
            if bin_digit:
                digits += "1"
            else:
                digits += "0"
        return digits

    def bool_list_to_int(self, bool_list: List[bool]) -> int:
        return int(self.bool_list_to_str(bool_list), 2)

    @property
    def oxygen_generator_rating(self):
        return self.calculate_rating(self.calculate_most_common_digits)

    @property
    def co2_scrubber_rating(self):
        return self.calculate_rating(self.calculate_least_common_digits)

    @property
    def life_support_rating(self):
        return self.oxygen_generator_rating * self.co2_scrubber_rating

    def calculate_rating(self, bit_criteria) -> int:
        """
        Determines the oxygen generator rating
        """
        values = copy.deepcopy(self.binary_data)

        for bit_position in range(self.width):
            most_common_value = bit_criteria(values)[bit_position]
            for value in copy.deepcopy(values):
                if value[bit_position] != most_common_value and len(values) > 1:
                    values.remove(value)

            if len(values) == 1:
                continue

        out = values[0]

        return self.bool_list_to_int(out)
