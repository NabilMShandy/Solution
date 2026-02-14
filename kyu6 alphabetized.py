def alphabetized(s):
    newS = s.replace(" ", "")
    newLs = []
    orderedLS = [x for x in sorted(newS, key=str.lower)]
    
    for item in orderedLS:
        if item.isalpha():
            newLs.append(item)

    strLS = str("".join(newLs))
    return strLS 



# The alphabetized kata
# Re-order the characters of a string, so that they are concatenated into a new string in "case-insensitively-alphabetical-order-of-appearance" order. Whitespace and punctuation shall simply be removed!
# The input is restricted to contain no numerals and only words containing the english alphabet letters.

# Example:
# alphabetized("The Holy Bible") # "BbeehHilloTy"