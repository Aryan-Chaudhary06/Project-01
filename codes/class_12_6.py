"""
WAP to read 3 digit nos. and make a dictionary with the middle digit as key and value the nos. 
having the same middle no.
"""
n = int(input("Enter no of elements: "))
l = []
for i in range(n):
    a = input()
    while a.isdigit == False and len(a) != 3:
        if a.isdigit == False:
            print("Enter a number.")
            a = input()
        if len(a) != 3:
            print("Enter a 3 digit no.")
            a = input()
    l.append(a)

d = {}
for ele in l:
    l1 = []
    for e in l:
        if ele[1] == e[1]:
            l1.append(e)
    d[ele[1]] = d.get(ele,l1)
print(d)