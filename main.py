#Function to open the file
def get_book_text(bookfile):
    with open(bookfile) as f:
        book = f.read()
    return book


#The main function that will print the book to the console
def main ():
    book = get_book_text('books/frankenstein.txt')
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
