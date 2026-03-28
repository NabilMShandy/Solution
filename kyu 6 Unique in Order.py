# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# Example
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

# Solution
def unique_in_order(sequence):
    if sequence == "" or sequence == [] or sequence == ():
        return []
    else:
        newvar = []
        for i in range(len(sequence)-1):
            if sequence[i] != sequence[i+1]:
                newvar.append(sequence[i])
        newvar.append(sequence[len(sequence)-1])
        
        return newvar