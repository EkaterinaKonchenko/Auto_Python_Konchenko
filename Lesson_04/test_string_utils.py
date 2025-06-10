import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("str_input", ["    Lesson4"])
def test_trim_positive(str_input):
    assert string_utils.trim(str_input) == "Lesson4"


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "p", "skyro"),
    ("hello world", "world", "hello "),
    ("python", "th", "pyon"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "p", True),
    ("hello world", "world", True),
    ("python", "sky", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("str_input", ["Lesson4      Lesson4"])
def test_trim_negative(str_input):
    assert string_utils.trim(str_input) == "Lesson4      Lesson4"


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "m", "skypro"),
    ("123 world", "0", "123 world"),
    ("_Python", "z", "_Python"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("123 skypro", "123", True),
    (":-))", ")", True),
    ("РУС#  ", " ", True),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected
    