"""
WAP to create a list and while creating the list it remains sorted.(without using sort())
"""
l=[]
n = int(input("Enter no. of lines: "))
for i in range(n):
    l.append(int(input()))
    while i>0:
      if l[i]<l[i-1]:
        a=l[i]
        l.pop(i)
        l.insert(i-1,a)
      i-=1
print(l)