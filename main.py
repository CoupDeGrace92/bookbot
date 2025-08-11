#Function to open the file
def get_book_text(bookfile):
    with open(bookfile) as f:
        book = f.read()
    return book


def char_count(book):
    word_list = book.split()
    word_string = "".join(word_list)
    word_list2 = word_string.lower()
    character_list = {}
    from stats import number_of_words
    i = number_of_words(book)-1 #This will be our list of total elements in our word_list
    for j in range(0,i):
        word = word_list2[j]
        length = len(word)
        for k in range(0, length-1):
            if word[k] in character_list:
                character_list[word[k]] = character_list[word[k]] + 1
            else:
                character_list[word[k]] = 1
    return character_list

#The main function that will print the book to the console
def main ():
    book = get_book_text('books/frankenstein.txt')
    from stats import number_of_words
    words = number_of_words(book)
    print (f"{words} words found in the document")
    #from stats import char_count
    char_dict = char_count(book)
    print (char_dict)
    return

main ()