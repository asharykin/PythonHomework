from collections import Counter
from re import sub


def count_unique_words(input_string):
    cleaned_string = sub(r"[^\w\s]", "", input_string.lower())
    words = cleaned_string.split()
    unique_words_count = len(Counter(words))
    return unique_words_count
