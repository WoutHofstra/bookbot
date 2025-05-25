import sys
from stats import get_num_chars
from stats import get_num_words
from stats import sorting_chars

def main():
    
    if len(sys.argv) == 2:
        book_text = get_book_text(sys.argv[1])
        num_words = get_num_words(book_text)
        num_chars = get_num_chars(book_text)
        sorted_list = sorting_chars(num_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for char in sorted_list:
            character = char["char"]
            count = char["num"]

            if character.isalpha():
                print(f"{character}: {count}")

        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    return None


def get_book_text(file_path):
    
    with open(file_path) as f:
        book_text = f.read()

    return book_text

if __name__ == "__main__":
    main()
