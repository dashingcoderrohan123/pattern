rows = int(input("Enter the number of rows: "))

if rows % 2 == 0:
    halfdiarow = int(rows / 2)
else:
    halfdiarow = int(rows / 2) + 1


space = halfdiarow - 1


for h in range(1, halfdiarow + 1):
    for n in range(1, space + 1):
        print(end=" ")  
    space = space - 1  
    
    num = 1
    for n in range(2 * h - 1):
        print(end=str(num)) 
        num = num + 1
    print()  


space = 1 
for h in range(1, halfdiarow):
    for n in range(1, space + 1):
        print(end=" ")  
    space = space + 1 
    num = 1
    for n in range(2 * (halfdiarow - h) - 1):
        print(end=str(num))  
        num = num + 1 
    print()  
