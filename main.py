import sys

from stats import count_words
from stats import count_characters, sort_char_counts

def get_book_text(filepath: str) -> str:
    """Read the contents of a text file and return it as a single string."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]  # take the path from CLI argument

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    book_text = get_book_text(filepath)

    # Word count
    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count
    char_counts = count_characters(book_text)
    sorted_char_counts = sort_char_counts(char_counts)

    print("--------- Character Count -------")
    for item in sorted_char_counts:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



# Call main() so the program runs when executed
if __name__ == "__main__":
    main()
