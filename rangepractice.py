
for i in range(1 , 11):
    print(i * "*")
print("========== print odd numbers from 1 to 50===================")

for i in range(1, 21, 2):
    print(i)

print("========== print table of 57===================")

for i in range(1, 11):
    print(57*i)    


print("========== mutlitples of 3, 1 to 50 skip 15===================")

for i in range(3, 51, 3):
    if i ==15:
        continue
    print(i)
a = int(input("Enter first number a: "))   
b = int(input("Enter second number b:"))
    
print("========== list of numbers divisible by both ", a, "and ", b)
for i in range(1 , 1001):
    if (i % a == 0) and (i % b == 0):
        print(i)
