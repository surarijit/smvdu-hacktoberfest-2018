# Program to find the ASCII value of the given character

# Insert a char to be converted
c = raw_input('Insert 1 character: ')
while len(c) > 1:
    print '1 char allowed'
    c = raw_input('Insert 1 character: ')

print("The ASCII value of '" + c + "' is",ord(c))
