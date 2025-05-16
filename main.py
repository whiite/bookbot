from stats import word_count, char_count, content_chars
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def report(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book = get_book_text(book_path)
    print("----------- Word Count ----------")
    print(f"Found {word_count(book)} total words")
    print("--------- Character Count -------")
    for char_count in content_chars(book):
        char = char_count["char"]
        count = char_count["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    report(path)


main()
