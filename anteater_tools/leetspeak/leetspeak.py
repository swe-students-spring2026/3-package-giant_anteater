LEET_MAP_LEVEL_1 = {
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
    's': '5',
}

LEET_MAP_LEVEL_2 = {
    **LEET_MAP_LEVEL_1,
    'b': '8',
    'g': '9',
    'l': '1',
    't': '7',
    'z': '2',
}


def to_leetspeak(text: str, level: int = 1) -> str:
    if level not in (1, 2):
        raise ValueError(f"level must be 1 or 2, got {level}")
    leet_map = LEET_MAP_LEVEL_1 if level == 1 else LEET_MAP_LEVEL_2
    return ''.join(leet_map.get(char.lower(), char) for char in text)


def from_leetspeak(text: str, strict: bool = False) -> str:
    reverse_map = {v: k for k, v in LEET_MAP_LEVEL_2.items()}
    result = []
    for char in text:
        if char in reverse_map:
            result.append(reverse_map[char])
        elif strict and char.isdigit():
            raise ValueError(f"Unknown leet digit '{char}' with strict=True")
        else:
            result.append(char)
    return ''.join(result)


def leet_score(text: str) -> float:
    if not text:
        return 0.0
    leet_chars = set(LEET_MAP_LEVEL_2.values())
    count = sum(1 for char in text if char in leet_chars)
    return count / len(text)


def is_leetspeak(text: str, threshold: float = 0.5) -> bool:
    if not (0.0 <= threshold <= 1.0):
        raise ValueError(f"threshold must be between 0.0 and 1.0, got {threshold}")
    return leet_score(text) >= threshold
