import random
import re


def _validate_mode(mode: str) -> None:
    if mode not in {"inner", "full"}:
        raise ValueError("mode must be either 'inner' or 'full'")


def _apply_case_pattern(scrambled: str, original: str) -> str:
    if original.isupper():
        return scrambled.upper()

    if original.islower():
        return scrambled.lower()

    if original[0].isupper() and original[1:].islower():
        return scrambled.capitalize()

    result = []
    for i, ch in enumerate(scrambled):
        if i < len(original) and original[i].isupper():
            result.append(ch.upper())
        else:
            result.append(ch.lower())
    return "".join(result)


def _shuffle_until_changed(chars: list[str], rng: random.Random, max_attempts: int = 10) -> list[str]:
    original = chars[:]
    for _ in range(max_attempts):
        rng.shuffle(chars)
        if chars != original:
            return chars
    return chars


def _scramble_letters(
    word: str,
    mode: str,
    preserve_short: bool,
    preserve_case: bool,
    rng: random.Random,
) -> str:
    _validate_mode(mode)

    if preserve_short and len(word) <= 3:
        return word

    if len(word) <= 1:
        return word

    base = word.lower()

    if mode == "full":
        chars = list(base)
        chars = _shuffle_until_changed(chars, rng)
        scrambled = "".join(chars)
    else:
        if len(base) <= 3:
            scrambled = base
        else:
            first = base[0]
            middle = list(base[1:-1])
            last = base[-1]
            middle = _shuffle_until_changed(middle, rng)
            scrambled = first + "".join(middle) + last

    if preserve_case:
        return _apply_case_pattern(scrambled, word)

    return scrambled


def scramble_word(
    word: str,
    mode: str = "inner",
    preserve_short: bool = True,
    preserve_case: bool = True,
    seed: int | None = None,
) -> str:
    """
    Scramble a single alphabetic word.

    mode
    "inner" keeps the first and last letters fixed
    "full" scrambles the whole word
    """
    if not isinstance(word, str):
        raise TypeError("word must be a string")

    if not word:
        raise ValueError("word must not be empty")

    if not word.isalpha():
        raise ValueError("word must contain letters only")

    rng = random.Random(seed)
    return _scramble_letters(word, mode, preserve_short, preserve_case, rng)


def scramble_text(
    text: str,
    mode: str = "inner",
    preserve_short: bool = True,
    preserve_case: bool = True,
    seed: int | None = None,
) -> str:
    """
    Scramble every alphabetic word in a string while preserving
    spaces and punctuation.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    _validate_mode(mode)
    rng = random.Random(seed)

    def replace(match: re.Match) -> str:
        word = match.group(0)
        return _scramble_letters(word, mode, preserve_short, preserve_case, rng)

    return re.sub(r"[A-Za-z]+", replace, text)


def count_changed_words(
    original_text: str,
    scrambled_text: str,
    ignore_case: bool = True,
) -> int:
    """
    Count how many alphabetic words changed between two texts.
    """
    if not isinstance(original_text, str) or not isinstance(scrambled_text, str):
        raise TypeError("both inputs must be strings")

    original_words = re.findall(r"[A-Za-z]+", original_text)
    scrambled_words = re.findall(r"[A-Za-z]+", scrambled_text)

    if len(original_words) != len(scrambled_words):
        raise ValueError("texts must contain the same number of words")

    changed = 0
    for left, right in zip(original_words, scrambled_words):
        if ignore_case:
            if left.lower() != right.lower():
                changed += 1
        else:
            if left != right:
                changed += 1

    return changed


def scramble_report(
    text: str,
    mode: str = "inner",
    preserve_short: bool = True,
    preserve_case: bool = True,
    seed: int | None = None,
) -> dict:
    """
    Return a report describing how the text was scrambled.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    scrambled = scramble_text(
        text,
        mode=mode,
        preserve_short=preserve_short,
        preserve_case=preserve_case,
        seed=seed,
    )

    original_words = re.findall(r"[A-Za-z]+", text)
    scrambled_words = re.findall(r"[A-Za-z]+", scrambled)

    changed_pairs = []
    for original, changed in zip(original_words, scrambled_words):
        if original.lower() != changed.lower():
            changed_pairs.append((original, changed))

    return {
        "original_text": text,
        "scrambled_text": scrambled,
        "mode": mode,
        "total_words": len(original_words),
        "changed_words": len(changed_pairs),
        "changed_pairs": changed_pairs,
    }