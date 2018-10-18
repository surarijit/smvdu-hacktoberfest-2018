def count(string,char):
    count=0
    for letter in string:
        if letter==char:
            count=count+1
    return count
a=input('enter the string: ')
b=input('enter the character you want to search: ')
print(count(a,b))
