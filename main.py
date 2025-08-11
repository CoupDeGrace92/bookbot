#Function to open the file
def get_book_text(bookfile):
    with open(bookfile) as f:
        book = f.read()
    return book

def number_of_words(book):
    word_list = book.split()
    words = len(word_list)
    return words


#The main function that will print the book to the console
def main ():
    book = get_book_text('books/frankenstein.txt')
    words = number_of_words(book)
    print (f"{words} words found in the document")
    return

main ()