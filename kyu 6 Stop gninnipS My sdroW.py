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