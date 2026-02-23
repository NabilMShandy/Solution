def xo(s):
    counterX=0
    counterO=0
    for i in s:
        if i=='X' or i=='x':
            counterX+=1
        elif i=='O' or i=='o':
            counterO+=1
    if counterX==counterO:
        return True
    else:
        return False


# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false