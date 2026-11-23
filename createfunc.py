def check_even_odd(a):
    if(a%2 == 0):
        return True
    else:
        return False
        
num=int(input("Enter Number: "))
c=check_even_odd(num)
if(c):
    print(num, "Is Even Number")
else:
    print(num, "Is odd number")


st = "rainbow"
counter=0
for ch in st:
    if ch in "aeiouAEIOU":
        counter +=1;
print("Count of Vowels in ", st ," = ",counter)      


from collections import Counter
text = input("Enter a string: ").lower()
counts = Counter(ch for ch in text if ch in "aeiou")
print("Total:", sum(counts.values()))
print(dict(counts))


vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print("Number of vowels:", count)


def average_marks(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)

print(average_marks([80, 70, 90]))   # 80.0
print(average_marks([]))   


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))   # True
print(is_prime(30))   # False
    