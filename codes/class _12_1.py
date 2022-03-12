"""
WAP to take a multiple line string and find the no. of words having special character in it. Also print 
the line/word which is a palindrome?
"""
n = int(input("Enter no. of lines: "))
line = """"""
for i in range(n):
  line += input() + "\n"
sp_char = "@#$&"
l = line.split("\n")

for k in l:
  for j in k:
    if j in sp_char:
      print(k," has a special character- ",j)

for m in l:
  b = m.lower()
  a = b.split(" ")
  if a == a[::-1] and len(a)>1:
    print(m, "is a Palindrome")
  else:
    for c in a:
      if c == c[::-1] and len(c)>1:
        print(c, "is a Palindrome")