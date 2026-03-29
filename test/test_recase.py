import pytest
from anteater_tools.recase import randomize, alternate

# randomize()

def test_randomize_preserves_characters():
    result = randomize("hello world", seed=42)
    assert result.lower() == "hello world"

def test_randomize_seed_deterministic():
    assert randomize("hello", seed=1) == randomize("hello", seed=1)

def test_randomize_different_seeds_differ():
    assert randomize("hello world", seed=1) != randomize("hello world", seed=2)

def test_randomize_empty_string():
    assert randomize("", seed=0) == ""

def test_randomize_non_alpha_unchanged():
    result = randomize("123!@#", seed=0)
    assert result == "123!@#"

def test_randomize_threshold_zero_all_lower():
    assert randomize("HELLO", threshold=0.0) == "hello"

def test_randomize_threshold_one_all_upper():
    assert randomize("hello", threshold=1.0) == "HELLO"

def test_randomize_invalid_threshold():
    with pytest.raises(ValueError):
        randomize("test", threshold=1.5)
    with pytest.raises(ValueError):
        randomize("test", threshold=-0.1)

# alternate()

def test_alternate_default():
    assert alternate("hello") == "HeLlO"

def test_alternate_start_lower():
    assert alternate("hello", start_upper=False) == "hElLo"

def test_alternate_preserves_non_alpha():
    assert alternate("h e l l o") == "H e L l O"

def test_alternate_empty_string():
    assert alternate("") == ""

def test_alternate_single_char():
    assert alternate("a") == "A"
    assert alternate("a", start_upper=False) == "a"

def test_alternate_non_alpha_skipped():
    result = alternate("a1b2c")
    assert result == "A1b2C"
