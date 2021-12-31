"""
Testing Module for testing the depth module
"""

import pytest

from day_02.depth import Submarine, SubCommand, parse_commands  # type: ignore


def test_init_sub():
    Submarine(horizontal=0, depth=0)


def test_sub_cannot_fly():
    with pytest.raises(ValueError):
        Submarine(horizontal=0, depth=-1)


def test_self_equal():
    assert Submarine(horizontal=0, depth=0) == Submarine(horizontal=0, depth=0)
    assert Submarine(horizontal=2, depth=1) == Submarine(horizontal=2, depth=1)
    assert Submarine(horizontal=4, depth=5) == Submarine(horizontal=4, depth=5)
    assert Submarine(horizontal=5, depth=0) == Submarine(horizontal=5, depth=0)
    assert Submarine(horizontal=0, depth=7) == Submarine(horizontal=0, depth=7)
    assert Submarine(horizontal=0, depth=8) == Submarine(horizontal=0, depth=8)


def test_execute_command():
    sub = Submarine(0, 0)
    sub.execute(SubCommand("forward", 5))
    assert sub.horizontal == 5
    sub.execute(SubCommand("backward", 3))
    assert sub.horizontal == 2
    sub.execute(SubCommand("backward", 3))
    assert sub.horizontal == -1
    sub.execute(SubCommand("down", 3))
    assert sub.depth == 3
    sub.execute(SubCommand("up", 1))
    assert sub.depth == 2


def test_parse_commands():
    input_string: str = "forward 5\ndown 7\nup 7\nbackward 2\n"
    parsed_commands = parse_commands(input_string)
    assert parsed_commands == [
        SubCommand("forward", 5),
        SubCommand("down", 7),
        SubCommand("up", 7),
        SubCommand("backward", 2)
    ]
