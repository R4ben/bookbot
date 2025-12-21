from stats import count_words, count_charecters, sorted_list
import sys
def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    contents =  get_book_text(sys.argv[1])
    num_words = count_words(contents)
    char_count = count_charecters(contents)
    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...""")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_char = sorted_list(char_count)
    for char in sorted_char:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
    
main()
