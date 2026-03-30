import pytest

from anteater_tools.word_scrambler.word_scrambler import (
    scramble_word,
    scramble_text,
    count_changed_words,
    scramble_report,
)


def test_scramble_word_inner_mode():
    result = scramble_word("developer", mode="inner", seed=7)

    assert result[0].lower() == "d"
    assert result[-1].lower() == "r"
    assert sorted(result.lower()) == sorted("developer")
    assert result.lower() != "developer"


def test_scramble_word_full_mode():
    result = scramble_word("python", mode="full", seed=7)

    assert sorted(result.lower()) == sorted("python")
    assert result.lower() != "python"
    assert len(result) == 6


def test_scramble_word_preserve_short():
    result = scramble_word("cat", mode="full", preserve_short=True, seed=7)

    assert result == "cat"
    assert len(result) == 3
    assert result.isalpha()


def test_scramble_word_invalid_inputs():
    with pytest.raises(TypeError):
        scramble_word(123)

    with pytest.raises(ValueError):
        scramble_word("")

    with pytest.raises(ValueError):
        scramble_word("hello!")


def test_scramble_text_preserves_punctuation():
    text = "Hello, world! I code."
    result = scramble_text(text, mode="inner", preserve_short=True, seed=7)

    assert "," in result
    assert "!" in result
    assert "." in result
    assert len(result) == len(text)


def test_scramble_text_keeps_short_words_when_requested():
    text = "I am a happy coder"
    result = scramble_text(text, mode="full", preserve_short=True, seed=7)

    assert "I" in result
    assert "am" in result
    assert "a" in result


def test_scramble_text_changes_longer_words():
    text = "Happy coding always wins"
    result = scramble_text(text, mode="inner", preserve_short=True, seed=7)

    assert result != text
    assert len(result) == len(text)
    assert sorted(result.replace(" ", "").lower()) == sorted(text.replace(" ", "").lower())


def test_count_changed_words_basic():
    original = "Hello world from python"
    scrambled = scramble_text(original, mode="inner", preserve_short=True, seed=7)
    changed = count_changed_words(original, scrambled)

    assert isinstance(changed, int)
    assert changed >= 1
    assert changed <= 4


def test_count_changed_words_ignore_case_option():
    assert count_changed_words("Hello", "hEllo", ignore_case=True) == 0
    assert count_changed_words("Hello", "hEllo", ignore_case=False) == 1
    assert count_changed_words("cat dog", "cat dog", ignore_case=True) == 0


def test_count_changed_words_invalid_inputs():
    with pytest.raises(TypeError):
        count_changed_words("abc", 123)

    with pytest.raises(ValueError):
        count_changed_words("one two", "one")


def test_scramble_report_contents():
    report = scramble_report("Hello world from python", mode="inner", seed=7)

    assert isinstance(report, dict)
    assert report["original_text"] == "Hello world from python"
    assert "scrambled_text" in report
    assert report["mode"] == "inner"
    assert report["total_words"] == 4
    assert report["changed_words"] >= 1
    assert isinstance(report["changed_pairs"], list)


def test_scramble_report_respects_preserve_short():
    report = scramble_report("I am a coder", mode="full", preserve_short=True, seed=7)

    assert report["total_words"] == 4
    assert report["changed_words"] <= 1
    assert isinstance(report["scrambled_text"], str)


def test_scramble_report_invalid_input():
    with pytest.raises(TypeError):
        scramble_report(123, mode="inner")