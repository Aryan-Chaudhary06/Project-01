"""
WAP to take a sentence and find:
i)   the most occuring word.
ii)  2nd most occuring word.
iii) longest word.
iv)  Palindrome word.
v)   Indexes of all occurence of a substring.
"""

#User input sentence
s1 = input("Enter a sentence: ")
s = s1.lower()
l = s.split(" ")
#creating a dictionary with word as key and its frequency as value
d = {}
for ele in l:
    d[ele]=d.get(ele,0)+1

l_val = list(d.values())#list of value from dict
#most occuring word
l_mo = []
for key in d:
    if d[key] == max(l_val):
        l_mo.append(key)
print("The most occuring word:" ,l_mo)

#2nd most occuring word
l_2mo = []
l_val.remove(max(l_val))
for key in d:
    if d[key] == max(l_val):
        l_2mo.append(key)
print("The 2nd most oxxuring word: ",l_2mo)

#longest word
l_len = [] 
for i in l:
    l_len.append(len(i))
l_index = l_len.index(max(l_len))
print("Longest word: ", l[l_len.index(max(l_len))])

#Palindrome word
for i in l:
    if i == i[::-1]:
        print(i, " is a Palindrome")

#Indexes of all occurence of a substring
s_str = input("Enter a sunstring: ")
s_str = s_str.lower()
for i in range(len(s)):
    if s[i:i+len(s_str)] == s_str:
        print("Idexes: ",i,end=", ")