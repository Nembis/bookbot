from stats import get_num_words, count_character_frequency, sort_char_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(sys.argv[1])
    word_count = get_num_words(content)
    character_dict = count_character_frequency(content)
    sorted_char_list = sort_char_dict(character_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()