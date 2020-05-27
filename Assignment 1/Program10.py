import math
# Program to print first 10 numbers if the given geometric series

print("Enter the first number and the common ratio")
a = int(input("First Number = "))
r = int(input("Common ratio = "))
c = 0
l = []
print ("The first 10 numbers of GS are:")
while c < 10:
	l.append(a)
	a = a * r;
	c += 1
print (l)
