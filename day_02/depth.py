"""
Advent of Code 2021 Day 2: Dive!
"""

from pathlib import Path
from typing import List

from attrs import define, field, validators


@define
class SubCommand:
    direction: str = field(validator=validators.instance_of(str))
    amount: int = field(validator=validators.instance_of(int))


@define
class Submarine:
    horizontal: int
    depth: int = field(validator=validators.instance_of(int))  # type: ignore

    @depth.validator
    def cannot_go_above_waterline(self, attribute, value):
        if value < 0:
            raise ValueError("Submarines cannot fly above the waterline.")

    def execute(self, command: SubCommand):
        if command.direction == "forward":
            self.horizontal += command.amount
        elif command.direction == "backward":
            self.horizontal -= command.amount
        elif command.direction == "up":
            self.depth -= command.amount
        elif command.direction == "down":
            self.depth += command.amount


def read_input_file(filename: Path = Path("input.txt")) -> List[SubCommand]:
    """
    Reads the input file and parses the commands.
    Returns the sequence of commands parsed.
    """
    with open(filename, 'r') as input_file:
        return parse_commands(input_file.read())


def parse_commands(command_string: str) -> List[SubCommand]:
    out: List[SubCommand] = []
    for line in command_string.splitlines():
        direction, amount = line.split(" ")
        out.append(SubCommand(direction.lower(), int(amount)))
    return out


def run_challenge():
    commands = read_input_file()
    sub = Submarine(0,0)
    for command in commands:
        sub.execute(command)
    print(sub)

if __name__ == "__main__":
    run_challenge()