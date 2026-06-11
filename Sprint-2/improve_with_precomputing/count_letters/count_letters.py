from collections import Counter

def count_letters(s: str) -> int:
    freq = Counter(s)

    only_upper = set()

    for ch in freq:
        if is_upper_case(ch):
            if freq.get(ch.lower(), 0) == 0:
                only_upper.add(ch)

    return len(only_upper)

def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()