a=int(input("Too oruul: "))
b=0

for i in range(2, a):
    if a%i == 0:
        b=1

if a>1 and b==0:
    print("Anhnii too")
else:
    print("Anhnii too bish")