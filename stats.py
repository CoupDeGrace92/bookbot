##Function to count the words in a given book string##

def number_of_words(book):
    word_list = book.split()
    words = len(word_list)
    return words


##Function to count the number of instances of each letter##
def char_count(book):
    import string
    word_list = book.split()
    word_string = "".join(word_list)
    word_string = word_string.lower()
    
    #Translates punctuation to null characters
    translator = str.maketrans('','', string.punctuation)
    word_string = word_string.translate(translator)
    character_list = {}
    i = len(word_string)
    for j in range(0,i):
            if word_string[j] in character_list:
                character_list[word_string[j]] += 1
            else:
                character_list[word_string[j]] = 1
    return character_list
                
##Function that takes a dictionary of characters and counts and sorts them from highest occurence to lowest##
def char_sort(character_list):
     import operator
     sorted_character_list = sorted(character_list.items(), key=operator.itemgetter(1), reverse=True)
     return sorted_character_list