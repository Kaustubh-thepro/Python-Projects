# Multiplication Table
x = int(input("Please enter a number to get its table : "))

if x>0:
    for y in range (1,11):
        z = x*y
        print(x,'X',y,'=',z)
