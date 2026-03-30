from anteater_tools import (
    add_with_steps,
    to_leetspeak,
    from_leetspeak,
    leet_score,
    is_leetspeak,
    randomize,
    alternate,
    regex_to_string,
    scramble_word,
    scramble_text,
    count_changed_words,
    scramble_report,
)


def main():
    print("Addition Tutor")
    print(add_with_steps(123, 987))

    print("\nLeetspeak")
    text = "Software engineering is fun"
    leet_text = to_leetspeak(text, level=2)
    print("Original:", text)
    print("To leetspeak:", leet_text)
    print("Back from leetspeak:", from_leetspeak(leet_text))
    print("Leet score:", leet_score(leet_text))
    print("Is leetspeak:", is_leetspeak(leet_text, threshold=0.3))

    print("\nRecase")
    recase_text = "Anteater Tools"
    print("Randomize:", randomize(recase_text, seed=42, threshold=0.5))
    print("Alternate:", alternate(recase_text, start_upper=True))

    print("\nRegex to String")
    pattern = "[A-Z]{2}[0-9]{3}"
    generated = regex_to_string(pattern)
    print("Pattern:", pattern)
    print("Generated string:", generated)

    print("\nWord Scrambler")
    word = "Anteater"
    print("Scrambled word:", scramble_word(word, mode="inner", seed=42))

    original_text = "Scrambling words can still be readable."
    scrambled_text = scramble_text(original_text, mode="inner", seed=42)
    print("Original text:", original_text)
    print("Scrambled text:", scrambled_text)
    print("Changed words:", count_changed_words(original_text, scrambled_text))
    print("Scramble report:", scramble_report(original_text, mode="inner", seed=42))


if __name__ == "__main__":
    main()