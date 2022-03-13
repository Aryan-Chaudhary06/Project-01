"""
WAP to merge content of two dictionaries
"""
n1 = int(input("Enter no of elements in dictonary1: "))
n2 = int(input("Enter no of elements in dictonary2: "))
d1 = {}
d2 = {}
for i in range(n1):
    keys = input("Enter a Key(str): ")
    value = int(input("Enter a value(int): "))
    d1[keys] = [value]
print(d1)
for i in range(n2):
    keys = input("Enter a Key(str): ")
    value = int(input("Enter a value(int): "))
    d2[keys] = [value]
print(d2)

print(d1 | d2)