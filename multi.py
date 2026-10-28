n = int(input("Enter a number: ")) #multiplication in order

i = 1

while(i<11):
    print(f"{n} X {i} = {n * i}")
    i += 1

n = int(input("Enter the number: ")) #multiplication in revers order

for i in range(1, 11):
    print(f"{n} X {11 -i} = {n*(11-i)}")