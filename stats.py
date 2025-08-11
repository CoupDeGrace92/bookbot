##Function to count the words in a given book string##

def number_of_words(book):
    word_list = book.split()
    words = len(word_list)
    return words


##Function to count the number of instances of each letter##
def char_count(book):
    word_list = book.split()
    word_list2 = word_list.lower()
    character_list = {}
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
                
