def get_book_text(bookfile):
    with open(bookfile) as f:
        book = f.read()
    return book



def number_of_words(book):
    word_list = book.split()
    words = len(word_list)
    return words

def char_count(book):
    import string
    word_list = book.split()
    word_s = "".join(word_list)
    word_s = word_s.lower()
    #word_s = word_s.translate(None, word_s.punctuation)
    print (len(word_s))
    #print (word_s)
    character_list = {}
    #len_str = len(word_s)
    #for j in range(0,len_str-1):
        #letter = word_s[j]
        #if letter in character_list:
        #    character_list[letter[j]] = character_list[letter[j]]+1
        #else:
        #    character_list[letter[j]] = 1
    

#    for j in range(0,i):
#        word = word_list2[j]
#        length = len(word)
#        for k in range(0, length-1):
#            if word[k] in character_list:
#              character_list[word[k]] = character_list[word[k]] + 1
#            else:
#                character_list[word[k]] = 1


    print (character_list)
    return character_list

def main ():
    book = get_book_text('books/frankenstein.txt')
    from stats import number_of_words
    words = number_of_words(book)
    print (f"{words} words found in the document")
    char_dict = char_count(book)
    print (char_dict)
    return

main ()