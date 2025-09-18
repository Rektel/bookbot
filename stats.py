
def count_words(text: str) -> int:
    """Count the number of words in a given text string."""
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict:
    """Return a dictionary mapping each character (lowercased) to its frequency."""
    char_counts = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1
    return char_counts

def sort_char_counts(char_counts: dict) -> list:
    """Return a sorted list of dictionaries (char + num) from greatest to least by count."""
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # only include alphabetic characters
            sorted_list.append({"char": char, "num": count})

    # Sort in place by "num" in descending order
    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list
