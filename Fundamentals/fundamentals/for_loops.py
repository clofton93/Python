for x in range(0, 151):
    print(x)
    
for x in range(5, 1000, 5):
    print(x)


for x in range(1, 100):
    if (x%5==0):
        print("Coding", x)
        
for x in range(0, 500000 + 1):
    if x % 2 != 0:
        print(x,)

y = 2018
while y > 0:
    print(y)
    y = y - 4
    if y == 0:
        break
    
    lownum = 2
    highnum = 9
    mult =3
    
    for x in range(lownum, highnum, mult):
        if (x%mult==0):
            print(x)