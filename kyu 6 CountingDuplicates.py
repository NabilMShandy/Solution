def duplicate_count(text):
    # one occur to checking an element whether is occurs once or else
    oneOccur = set()
    # duplicate using set to adding the element if its exist
    duplicate = set()
    # using iteration for element in text with lowercase 
    for element in text.lower():
        # if an element is occurs on set, add it to duplicate set
        if element in oneOccur:
            duplicate.add(element)
        # else, add it to one occur set
        else:
            oneOccur.add(element)
    # to know how many are the elements that are duplicate, we can use the length of duplicate set as well
    return len(duplicate)

print(duplicate_count("Indivisibilities"))
print(duplicate_count("indivisibility"))
print(duplicate_count("aA11"))
print(duplicate_count("ABBA"))
print(duplicate_count("abcde"))

# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# # abcde" -> 0 # no characters repeats more than once
# # "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice