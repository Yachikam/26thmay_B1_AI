#TASK 1:

#Find the count of each character

#Check if all the counts are same or at most one character is one extra than
#all the others, Its MYSTRING else NOT MYSTRING.

a = input('Enter any characters: ')
b = {i:a.count(i) for i in a}
print(b)

c = list(b.values())
d = set(c)

print("MYSTRING") if (max(c)-min(c)<=1 and (c.count(max(c))==1 or len(d)==1)) else print("NOT MYSTRING")
