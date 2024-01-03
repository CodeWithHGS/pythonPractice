n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            if j==i:
                print(i,end=" ")
            else:
                print(i,end="*")
    print()