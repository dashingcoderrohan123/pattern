#Write a program to demonstrate a Floyd triangle pattern?
#floyd's triangle is a right angle triangle which holds natural numbers in consecutive order                   

rows=int(input("Please enter the number of rows you want"))
number=1
print("Floyd Tringle")

for y in range(1,rows+1):
    for v in range(1,y+1):
        print(number,end="")
        number=number+1
    print()     