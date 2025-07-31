# first unique char

def unique(s):
    for ch in s:
        if s.count(ch)==1 :
            return ch
    return ('no unique')
        
print(unique('vasidvsa'))
            
# another way to do it 

def first_unique(ch):
    for index, i in enumerate(ch):
        print(index, i)
    return -1

print(first_unique('shah'))


# print 1 to 50
''' Write a program that prints the numbers from 1 to 50.
But for multiples of 3, print "Fizz" instead of the number,
for multiples of 5, print "Buzz",'''

def num_Printing(no):
    for i in range(no):
        if i%3 ==0:
            print('fizz')
        elif i%5 ==0:
            print('bizzz')
        else:
            print(i)

#print(num_Printing(50))

# print star pattern

def star_pattern(no):
    for i in range(no):
        for j in range(no):
            print('*', end = '')
        print()

print(star_pattern(6))


# trange star pattern

def trangle(n):
    for i in range(1,1+n):
        for j in range(i):
            print('*', end = '')
        print()

print(trangle(5))
    
# print no 1 to 10 using while loop 

n=1
while n<= 10:
    print(n)
    n += 1

# by defining function
def num(no):
    n=1
    while n<no:
        print(n)
        n+=1

print(num(12))


# sum of  n no 
def sum(n):
    total = 0
    i = 1
    while 1 <=n:
        total += i
        i +=1
    return total
print(sum(10))


# palindrome 
def palindrome(str):
    return str== str[::-1]

palindrome(12453)
# sort list without sort function 

def sort_list(num):
    sor_list = []
    for i in num:
        if i not in sor_list:
            sor_list.append(i)
    sor_list.sort()
    return sor_list

print(sort_list([1,5,6,8,4,7,3,5,9,2]))

