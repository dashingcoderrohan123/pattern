#Write a program to demonstrate a right angle triangle pattern?

print("half piramid patterns of stars(*)")
rows=int(input("enter the no of rows"))


for i in range(rows):
    for k in range(i+1 ):
        print("*",end="")

    print()