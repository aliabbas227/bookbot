from collections import Counter

def get_num_words(text):
    return f"Found {len(text.split())} total words"     # returns the length of array from using split.

def get_char_freq(text):
    text = text.lower()                                              # make text all lower case
    return dict(Counter(c for c in text if c.isalpha()))         # only counts letters

def sort_char_freq(freq):
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))    # Sort list from highest to lowest frequency

    for key, value in sorted_freq.items():
        print(f"{key}: {value}")