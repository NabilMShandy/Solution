def spin_words(sentence):
    newVar = " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split()])
    return newVar
    # Alternate solution
    # emptyLs = []
    # for i in sentenceSplit:
    #     if len(i) >= 5:
    #         emptyLs.append(i[::-1])
    #     else:
    #         emptyLs.append(i)
    # return " ".join(emptyLs)

print(spin_words("This sentence is a sentence"))


# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (just like the name of this kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
# Examples:
# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"