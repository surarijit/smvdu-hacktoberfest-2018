def binary(n):
  for x in range(1,n+1):
    a = bin(x)
    a=list(a)
    #b=''.append(a)
    del(a[0])
    del(a[0])
    b=''.join(a)
    print(b)

binary(2)