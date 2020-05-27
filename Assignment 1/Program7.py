
# Find the armstrong numbers within a range

# Armstrong number is a number that is equal to the sum of cubes of its digits.
# For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

print('Enter the range\n')
n = int(input('From : '))
m = int(input('To : '))
def is_armstrong(n) :
    string = str(n)
    for i in string :
        n = n - pow(int(i), 3)
    if n == 0 :
        return True
    else :
        return False

list1 = []
for i in range(n, m + 1) :
    if is_armstrong(i) :
        list1.append(i)

print(list1)