"""
Tests for Advent of Code 2021 Day 3
"""
import pytest

from day_03.binary_diagnostic import DiagnosticReport, parse_row  # type: ignore


def test_create_report():
    DiagnosticReport()
    d = DiagnosticReport(
        [
            [True, False, True],
            [True, True, True],
            [False, True, True]
        ]
    )
    assert d.width == 3
    with pytest.raises(ValueError):
        DiagnosticReport([[True, False], [True]])
    with pytest.raises(ValueError):
        DiagnosticReport([True, False], {True, False})


def test_parse_row():
    assert parse_row('0') == [False]
    assert parse_row('1') == [True]
    assert parse_row('01') == [False, True]
    assert parse_row('10') == [True, False]
    with pytest.raises(ValueError):
        parse_row('20')

def test_parse_append():
    d = DiagnosticReport()
    d.append_line("01010")
    assert d.width == 5
    assert d.binary_data == [[False, True, False, True, False]]
    d.append_line("10101")
    assert d.binary_data == [[False, True, False, True, False],
                             [True, False, True, False, True]]


def test_parse_multiline():
    d = DiagnosticReport()
    d.append_multiline("01\n10\n11\n")
    assert d.binary_data == [[False, True], [True, False], [True, True]]


def test_append_wrong_row_width():
    d = DiagnosticReport([[True, False]])
    with pytest.raises(ValueError):
        d.append_line('1')
    with pytest.raises(ValueError):
        d.append_line('101')
    with pytest.raises(ValueError):
        d.append_multiline('01\n11\n101\n01')


def test_gamma_rate():
    d = DiagnosticReport.from_str('101\n111\n001')
    assert d.gamma_rate == int('101', 2)
    d.append_multiline('111\n111')
    assert d.gamma_rate == int('111', 2)


def test_epsilon_rate():
    d = DiagnosticReport([
        [True, True, True],
        [True, True, False],
        [True, False, False]
    ])
    assert d.epsilon_rate == int('001', 2)


def test_official_example():
    example_input = "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010"
    d = DiagnosticReport.from_str(example_input)
    assert d.gamma_rate == 22
    assert d.epsilon_rate == 9
    assert d.power_consumption == 22 * 9


def test_with_input_file():
    input_text = open('day_03/input.txt', 'r').read()
    report = DiagnosticReport.from_str(input_text)
    assert report.power_consumption == 3277364
