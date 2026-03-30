import random
from typing import Hashable, Optional


def randomize(text: str, seed: Optional[Hashable] = None, threshold: float = 0.5) -> str:
    """Randomly converts each character to upper or lower case.

    threshold controls the probability of uppercasing (0.0 = all lower, 1.0 = all upper).
    """
    if not (0.0 <= threshold <= 1.0):
        raise ValueError(f"threshold must be between 0.0 and 1.0, got {threshold}")
    rng = random.Random(seed)
    return ''.join(
        char.upper() if rng.random() < threshold else char.lower()
        for char in text
    )


def alternate(text: str, start_upper: bool = True) -> str:
    """Alternates the case of each letter. Non-alpha characters are kept but don't affect the pattern."""
    result = []
    upper = start_upper
    for char in text:
        if char.isalpha():
            result.append(char.upper() if upper else char.lower())
            upper = not upper
        else:
            result.append(char)
    return ''.join(result)
