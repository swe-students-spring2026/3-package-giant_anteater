import re
import pytest

from anteater_tools.regex_to_string import regex_to_string


def contains_special_regex_characters(s: str) -> bool:
    special_chars = set(".^$*+?{}[]\\|()")
    return any(ch in special_chars for ch in s)


def test_plain_literal_pattern():
    result = regex_to_string("abc123")
    assert result == "abc123"
    assert re.fullmatch("abc123", result)
    assert not contains_special_regex_characters(result)


def test_character_class_pattern():
    result = regex_to_string("[abc][xyz]")
    assert len(result) == 2
    assert re.fullmatch("[abc][xyz]", result)
    assert not contains_special_regex_characters(result)


def test_range_pattern():
    result = regex_to_string("[a-z][0-9][A-Z]")
    assert len(result) == 3
    assert re.fullmatch("[a-z][0-9][A-Z]", result)
    assert not contains_special_regex_characters(result)


def test_question_quantifier():
    result = regex_to_string("a?b")
    assert re.fullmatch("a?b", result)
    assert result in {"b", "ab"}
    assert not contains_special_regex_characters(result)


def test_plus_quantifier():
    result = regex_to_string("[a-z]+")
    assert re.fullmatch("[a-z]+", result)
    assert len(result) >= 1
    assert not contains_special_regex_characters(result)


def test_star_quantifier():
    result = regex_to_string("[0-9]*")
    assert re.fullmatch("[0-9]*", result)
    assert not contains_special_regex_characters(result)


def test_exact_quantifier():
    result = regex_to_string("[a-z]{4}")
    assert len(result) == 4
    assert re.fullmatch("[a-z]{4}", result)
    assert not contains_special_regex_characters(result)


def test_range_quantifier():
    result = regex_to_string("[A-Z]{2,5}")
    assert 2 <= len(result) <= 5
    assert re.fullmatch("[A-Z]{2,5}", result)
    assert not contains_special_regex_characters(result)


def test_empty_pattern_raises_error():
    with pytest.raises(ValueError):
        regex_to_string("")


def test_non_string_pattern_raises_error():
    with pytest.raises(ValueError):
        regex_to_string(None)


def test_unclosed_character_class_raises_error():
    with pytest.raises(ValueError):
        regex_to_string("[abc")


def test_invalid_quantifier_range_raises_error():
    with pytest.raises(ValueError):
        regex_to_string("a{5,2}")


def test_unsupported_parentheses_raise_error():
    with pytest.raises(ValueError):
        regex_to_string("(ab)")