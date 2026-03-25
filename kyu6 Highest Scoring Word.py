# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.


# Solution
# maybe O(n^2)
def high(x):
    mydicts = {}
    xSplitter = x.split()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabets)):
        mydicts[alphabets[i]] = i+1
    
    sums = 0
    newls = []
    wordls = []
    for j in range(len(xSplitter)):
        newls.append(xSplitter[j])
        for k in range(len(" ".join(newls))):
            sums += mydicts[" ".join(newls)[k]]
        wordls.append(sums)
        sums = 0
        newls = []
        
    return xSplitter[wordls.index(max(wordls))]