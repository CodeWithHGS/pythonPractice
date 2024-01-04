n=int(input('Enter a number'))
for i in range(n):
    a=0
    for j in range(2*n-1):
        if j<=2*i:
            if j<i:
                print(chr(65+j),end="")
            if j==i:
                print(chr(65+j),end="")
            if j>i:
                print(chr(a+i-1+65),end="")
                a-=1
        else:
            print("",end="")
    print()