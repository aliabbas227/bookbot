def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = count_words(text)
    char_count = count_chars(text)
    char_list = sorted(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End Report ---")

#Used to turn text into string
def get_book_text(path):
    with open(path) as f:
        return f.read()

#Used to count words in text
def count_words(texts):
    word_counter = 0
    words = texts.split()
    for word in words:
        word_counter += 1
    return word_counter

#Used to count times a letter is used
def count_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_dict(dict):
    return dict["num"]

#Used to sort by number descending
def sorted(text):
    char_count = count_chars(text)
    char_list = [{"char":char,"num": count} for char,count in char_count.items()]
    char_list.sort(reverse=True,key=sort_dict)
    return char_list

main()

