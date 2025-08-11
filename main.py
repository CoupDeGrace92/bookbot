import string

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
    print (f"{words} words found in the document")
    from stats import char_count
    char_dict = char_count(book)
    print (char_dict)
    from stats import char_sort
    sorted_characters = char_sort(char_dict)
    print (sorted_characters)
    return

main ()