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

print(num_Printing(50))

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
    