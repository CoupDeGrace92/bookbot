##Function to count the words in a given book string##

def number_of_words(book):
    word_list = book.split()
    words = len(word_list)
    return words


##Function to count the number of instances of each letter##
def char_count(book):
    word_list = book.split()
    word_string = "".join(word_list)
    word_string = word_string.lower()
    character_list = {}
    i = len(word_string)
    for j in range(0,i):
            if word_string[j] in character_list:
                character_list[word_string[j]] += 1
            else:
                character_list[word_string[j]] = 1
    return character_list
                
