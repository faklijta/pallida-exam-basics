# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases

def unique_characters(word):
    word_list = list(word)
    word_list.sort()
    unique = []
    if len(word) <= 0 or word == None:
        return False
    for element in range(0, len(word_list)-1):
        if word_list[element] != word_list[element+1]:
            unique.append(word_list[element+1])
    return unique

    


print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]
