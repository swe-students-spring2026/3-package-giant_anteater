import random
import re
import string


SPECIAL_REGEX_CHARS = set(".^$*+?{}[]\\|()")


def _parse_char_class(content: str) -> list[str]:
    chars = []
    i = 0

    while i < len(content):
        if i + 2 < len(content) and content[i + 1] == "-":
            start = content[i]
            end = content[i + 2]
            chars.extend(chr(code) for code in range(ord(start), ord(end) + 1))
            i += 3
        else:
            chars.append(content[i])
            i += 1

    filtered = [ch for ch in chars if ch not in SPECIAL_REGEX_CHARS]
    return filtered


def _read_quantifier(pattern: str, i: int) -> tuple[int, int, int]:
    if i >= len(pattern):
        return 1, 1, i

    if pattern[i] == "?":
        return 0, 1, i + 1
    if pattern[i] == "*":
        return 0, 5, i + 1
    if pattern[i] == "+":
        return 1, 5, i + 1

    if pattern[i] == "{":
        j = i + 1
        while j < len(pattern) and pattern[j] != "}":
            j += 1
        if j == len(pattern):
            raise ValueError("Unclosed quantifier")

        content = pattern[i + 1 : j]
        if "," in content:
            left, right = content.split(",", 1)
            min_count = int(left.strip())
            max_count = int(right.strip())
        else:
            min_count = max_count = int(content.strip())

        if min_count > max_count:
            raise ValueError("Invalid quantifier range")

        return min_count, max_count, j + 1

    return 1, 1, i


def regex_to_string(pattern: str) -> str:
    """
    Generate a random string matching a supported subset of regular expressions.
    Supported syntax includes:
    - literal alphanumeric characters
    - character classes, e.g. [abc]
    - ranges, e.g. [a-z], [A-Z], [0-9]
    - quantifiers: ?, *, +, {m}, {m,n}
    """
    if not isinstance(pattern, str) or pattern == "":
        raise ValueError("Pattern must be a non-empty string")

    result = []
    i = 0

    while i < len(pattern):
        token_choices = []

        if pattern[i].isalnum():
            token_choices = [pattern[i]]
            i += 1

        elif pattern[i] == "[":
            j = i + 1
            while j < len(pattern) and pattern[j] != "]":
                j += 1
            if j == len(pattern):
                raise ValueError("Unclosed character class")

            content = pattern[i + 1 : j]
            token_choices = _parse_char_class(content)
            if not token_choices:
                raise ValueError("Character class does not contain valid output characters")
            i = j + 1

        else:
            raise ValueError(f"Unsupported pattern syntax: {pattern[i]}")

        min_count, max_count, i = _read_quantifier(pattern, i)
        repeat_count = random.randint(min_count, max_count)

        for _ in range(repeat_count):
            result.append(random.choice(token_choices))

    generated = "".join(result)

    if any(ch in SPECIAL_REGEX_CHARS for ch in generated):
        raise ValueError("Generated string contains regex special characters")

    if not re.fullmatch(pattern, generated):
        raise ValueError("Generated string does not match the pattern")

    return generated