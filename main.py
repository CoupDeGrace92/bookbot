import sys

#Function to open the file
def get_book_text(bookfile):
    with open(bookfile) as f:
        book = f.read()
    return book


#The main function that will print the book to the console
def main ():
    try:
        book = sys.argv[1]
    except Exception:
        print('No book found')
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    book = get_book_text(sys.argv[1])
    from stats import number_of_words
    words = number_of_words(book)
    from stats import char_count
    char_dict = char_count(book)
    from stats import char_sort
    from stats import pretty_output
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print (f"Found {words} total words")
    print("--------- Character Count -------")
    pretty_output(char_dict)
    print("============= END ===============")
    return

main ()
