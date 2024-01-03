n=int(input("Enter a Number: "))
for i in range(2*n+1):
    for j in range(2*n+1):
        if j<n-i or j>n+i or j<i-n or j>2*n-(i-n):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# Comment added by leeenu