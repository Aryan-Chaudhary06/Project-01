"""
WAP to take a list of nos. and find the no wich is a multiply of 5 and move one index back
Eg. l =[3,15,4,2,5]
output --> [15,3,4,5,2]
"""
n = int(input("Enter no. of elements: "))
l = []
for ele in range(n):
    l.append(int(input()))
for i in range(len(l)):
    if l[i]%5 == 0 and i != 0:
        a = l[i]
        l.remove(a)
        l.insert(i-1,a)
print(l)