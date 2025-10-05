# Import functions
from stats import get_num_words, get_char_freq, sort_char_freq
import sys

def get_book_text(file_path):
    with open(file_path) as f:      # Open file
        file_contents = f.read()    # Convert file to string
    return file_contents

def print_report(file_path):
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    char_freq = get_char_freq(text)

    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count -----------")
    print(num_words)
    print("--------- Character Count --------")
    sorted_char_freq = sort_char_freq(char_freq)
    print("============= END ================")


def main():
    if len(sys.argv) < 2:                                       # makes sure your using main.py and <filepath>
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    file_path = sys.argv[1]                                     # Uses 2nd argument as file_path

    print_report(file_path)


main()