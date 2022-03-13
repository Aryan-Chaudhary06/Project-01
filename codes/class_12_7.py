"""
WAP to take a dictionary with homologeous values and print the key corresponding to the 3 highest
value.
"""
from sys import dllhandle


n = int(input("Enter no. of elements: "))
type_ = input("Enter the type of values - (s) for string and (i) for integers: ")
type_ = type_.lower()
d ={}
for i in range(n):
    key = input("Enter key: ")
    if type_ == "s":
        value = input("Enter value: ")
    elif type_ == "i":
        value = int(input("Enter value: "))
    d[key] = value

print(d)
l = list(d.values())
l.sort(reverse=True)

for i in range(3):
    for key in d:
        if d[key] == l[i]:
            print(key,":",d[key])
