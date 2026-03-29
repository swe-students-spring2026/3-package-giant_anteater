import pytest
from anteater_tools.leetspeak.leetspeak import to_leetspeak, from_leetspeak, leet_score, is_leetspeak



# to_leetspeak


def test_to_leetspeak_level1_basic():
    assert to_leetspeak("leet", level=1) == "l33t"

def test_to_leetspeak_level1_preserves_unmapped():
    result = to_leetspeak("hello world", level=1)
    assert result == "h3ll0 w0rld"
    assert ' ' in result

def test_to_leetspeak_level2_extra_substitutions():
    assert to_leetspeak("bit", level=2) == "817"
    assert to_leetspeak("bit", level=1) == "b1t"

def test_to_leetspeak_case_insensitive():
    assert to_leetspeak("ELITE", level=1) == "3L1T3"
    assert to_leetspeak("Elite", level=2) == "31173"

def test_to_leetspeak_invalid_level():
    with pytest.raises(ValueError):
        to_leetspeak("test", level=0)
    with pytest.raises(ValueError):
        to_leetspeak("test", level=3)

def test_to_leetspeak_empty_string():
    assert to_leetspeak("", level=1) == ""
    assert to_leetspeak("", level=2) == ""



# from_leetspeak


def test_from_leetspeak_reverses_level2():
    assert from_leetspeak("1337") == "leet"

def test_from_leetspeak_passthrough_unknown():
    result = from_leetspeak("x3x")
    assert result == "xex"
    assert 'x' in result

def test_from_leetspeak_strict_raises_on_unknown_digit():
    with pytest.raises(ValueError):
        from_leetspeak("6", strict=True)

def test_from_leetspeak_strict_false_allows_unknown_digit():
    result = from_leetspeak("6", strict=False)
    assert result == "6"

def test_from_leetspeak_empty_string():
    assert from_leetspeak("") == ""
    assert from_leetspeak("", strict=True) == ""



# leet_score


def test_leet_score_fully_leet():
    assert leet_score("1337") == 1.0

def test_leet_score_no_leet():
    score = leet_score("xyz")
    assert score == 0.0

def test_leet_score_partial():
    score = leet_score("h3llo")
    assert score == pytest.approx(0.2)

def test_leet_score_empty_string():
    assert leet_score("") == 0.0

def test_leet_score_bounds():
    score = leet_score("4ny str1ng")
    assert 0.0 <= score <= 1.0



# is_leetspeak


def test_is_leetspeak_above_threshold():
    assert is_leetspeak("1337") is True

def test_is_leetspeak_below_threshold():
    assert is_leetspeak("hello") is False

def test_is_leetspeak_custom_threshold():
    assert is_leetspeak("h3llo", threshold=0.1) is True
    assert is_leetspeak("h3llo", threshold=0.3) is False

def test_is_leetspeak_invalid_threshold():
    with pytest.raises(ValueError):
        is_leetspeak("test", threshold=1.5)
    with pytest.raises(ValueError):
        is_leetspeak("test", threshold=-0.1)

def test_is_leetspeak_empty_string():
    assert is_leetspeak("", threshold=0.5) is False
    assert is_leetspeak("", threshold=0.0) is True
