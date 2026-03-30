# anteater-tools

[![Python package tests](https://github.com/swe-students-spring2026/3-package-giant_anteater/actions/workflows/python-app.yml/badge.svg)](https://github.com/swe-students-spring2026/3-package-giant_anteater/actions/workflows/python-app.yml)

A lighthearted Python utility package with five modules: a step-by-step addition tutor, a leetspeak converter, a text recaser, a regex-to-string generator, and a word scrambler.

**PyPI page:** [https://pypi.org/project/anteater-tools/](https://pypi.org/project/anteater-tools/)

---

## Installation

```bash
pip install anteater-tools
```

---

## Usage

See [example.py](./example.py) for a complete program that uses every function.

### Addition Tutor

```python
from anteater_tools import add_with_steps

print(add_with_steps(123, 987))
# Prints a formatted column-addition breakdown with carries and step-by-step explanations.

print(add_with_steps(55, 45, show_carry=False))
# Same layout but without the carry row.
```

**`add_with_steps(a, b, show_carry=True) -> str`**
Returns a formatted string showing column addition of two integers, including aligned digits, carry row, result, and per-column explanations. Set `show_carry=False` to hide the carry row.

---

### Leetspeak

```python
from anteater_tools import to_leetspeak, from_leetspeak, leet_score, is_leetspeak

text = "Software engineering is fun"
leet = to_leetspeak(text, level=2)   # "50ftw4r3 3ng1n33r1ng 15 fun"
back = from_leetspeak(leet)          # "software engineering is fun"
score = leet_score(leet)             # float between 0.0 and 1.0
check = is_leetspeak(leet, threshold=0.3)  # True or False
```

**`to_leetspeak(text, level=1) -> str`**
Converts text to leetspeak. `level=1` replaces a few common vowels (`a→4`, `e→3`, `i→1`, `o→0`, `s→5`). `level=2` adds more substitutions (`b→8`, `g→9`, `l→1`, `t→7`, `z→2`).

**`from_leetspeak(text, strict=False) -> str`**
Reverses leetspeak substitutions. With `strict=True`, raises `ValueError` on any unrecognized digit.

**`leet_score(text) -> float`**
Returns the fraction of characters that are leet substitutions (0.0–1.0).

**`is_leetspeak(text, threshold=0.5) -> bool`**
Returns `True` if `leet_score(text) >= threshold`.

---

### Recase

```python
from anteater_tools import randomize, alternate

randomize("Anteater Tools", seed=42, threshold=0.5)  # e.g. "ANteaTer tOolS"
alternate("Anteater Tools", start_upper=True)         # "AnTeAtEr tOoLs"
```

**`randomize(text, seed=None, threshold=0.5) -> str`**
Randomly uppercases or lowercases each character. `threshold` controls the probability of uppercasing (0.0 = all lower, 1.0 = all upper). Pass a `seed` for reproducible output.

**`alternate(text, start_upper=True) -> str`**
Alternates case letter by letter. Non-alphabetic characters are preserved but don't break the alternating pattern. `start_upper=False` begins with a lowercase letter.

---

### Regex to String

```python
from anteater_tools import regex_to_string

regex_to_string("[A-Z]{2}[0-9]{3}")   # e.g. "XK492"
regex_to_string("[a-z]{4,6}")         # e.g. "mwqrt"
```

**`regex_to_string(pattern) -> str`**
Generates a random string that matches the given pattern. Supports literal alphanumeric characters, character classes (`[abc]`, `[a-z]`, `[A-Z]`, `[0-9]`), and quantifiers (`?`, `*`, `+`, `{m}`, `{m,n}`).

---

### Word Scrambler

```python
from anteater_tools import scramble_word, scramble_text, count_changed_words, scramble_report

scramble_word("Anteater", mode="inner", seed=42)
# e.g. "Antaeetr" — first and last letters stay fixed

original = "Scrambling words can still be readable."
scrambled = scramble_text(original, mode="inner", seed=42)
count_changed_words(original, scrambled)   # number of words that changed
scramble_report(original, mode="inner", seed=42)
# returns a dict with original_text, scrambled_text, mode, total_words, changed_words, changed_pairs
```

**`scramble_word(word, mode="inner", preserve_short=True, preserve_case=True, seed=None) -> str`**
Scrambles a single alphabetic word. `mode="inner"` keeps the first and last letters fixed; `mode="full"` scrambles everything. Words of 3 letters or fewer are left alone when `preserve_short=True`.

**`scramble_text(text, mode="inner", preserve_short=True, preserve_case=True, seed=None) -> str`**
Applies `scramble_word` to every word in a string, leaving spaces and punctuation untouched.

**`count_changed_words(original_text, scrambled_text, ignore_case=True) -> int`**
Counts how many alphabetic words differ between two strings. Both strings must have the same number of words.

**`scramble_report(text, mode="inner", preserve_short=True, preserve_case=True, seed=None) -> dict`**
Returns a dictionary with keys: `original_text`, `scrambled_text`, `mode`, `total_words`, `changed_words`, `changed_pairs`.

---

## Getting Started

These instructions work on macOS, Linux, and Windows.

### Option 1: Install from PyPI

```bash
pip install anteater-tools
```

Then download and run the example program:

```bash
# download example.py from the repo, then:
python example.py
```

### Option 2: Run from source

```bash
git clone https://github.com/swe-students-spring2026/3-package-giant_anteater.git
cd 3-package-giant_anteater
pip install .
python example.py
```

`example.py` exercises every function in the package and prints output to the terminal. No environment variables, configuration files, or databases are required.

---

## Contributing

### Prerequisites

- Python 3.10+
- [pipenv](https://pipenv.pypa.io/)

### Set up the development environment

```bash
git clone https://github.com/swe-students-spring2026/3-package-giant_anteater.git
cd 3-package-giant_anteater
pipenv install --dev
```

This installs all dependencies and the package itself in editable mode.

### Run tests

```bash
pipenv run pytest
```

### Build the package

```bash
pipenv run python -m build
```

### Publish to PyPI (maintainers only)

```bash
pipenv run twine upload dist/*
```

### Developer workflow

1. Create a feature branch off `main`.
2. Make your changes and add tests.
3. Open a pull request to `main` and ask a teammate to review.
4. After approval and passing CI, merge and delete the feature branch.

---

## Team

- [Zelu Zhang](https://github.com/zzl0720-2025)
- [Teammate 2](https://github.com/teammate2)
- [Teammate 3](https://github.com/teammate3)
- [Teammate 4](https://github.com/teammate4)
- [Teammate 5](https://github.com/teammate5)
