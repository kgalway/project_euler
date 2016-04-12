def is_palindrome(n):
    digits = []
    while n:
        digits.append(n%10)
        n/=10
    i = True
    for j in xrange(len(digits)//2):
        i = i and (digits[j]==digits[-j-1])
    return i

def solution_4():
    highest = 0
    for i in xrange(999,99,-1):
        for j in xrange(999,99,-1):
            if is_palindrome(i*j):
                highest = max(highest, i*j)
    return highest 


def solution_7(nth_prime, max_iter = 100000000):
    """ outputs the nth prime """
    i=0
    primes = 0
    count = 0
    while primes < nth_prime:
        if i > max_iter:
            break
        primes += is_prime(i) 
        i+=1
    return i-1
    

def is_prime(n):
    if n<=3:
        if n<=1:
            return False
        return True
    if not n%2 or not n%3:
        return False
    for i in xrange(5,int(n**0.5)+1,6):
        if not n%i or not n%(i+2):
            return False
    return True 


def solution_24(n=1000000):
    import itertools
    nums = range(10)
    vals = []
    perms = itertools.permutations(nums)
    while perms:
        vals.append(perms.next())
    vals.sort()
    return vals[n]

def solution_9():
    """ find the unique pythagorean triplet for a + b + c = 1000
         return the value a*b*c """
    a = xrange(1,1001)
    b = xrange(1000,0,-1)
    for i in a:
        for j in b:
            c = 1000 - i - j
            if c < 0:
                continue
            else:
                if i**2 + j**2 == c**2:
                    print('solution found')
                    return i*j*c

def solution_22():
    import string 
    with open('names.txt','r') as f:
        names = f.read()
    f.close()
    names = names.upper()
    names = names.split(',')
    names.sort()
    letters = string.ascii_uppercase
    theTotal = 0
    nowTotal = 0
    for i,name in enumerate(names):
        for letter in name:
            nowTotal += letters.find(letter) + 1
        theTotal += nowTotal*(1+i)
        nowTotal = 0
    return theTotal


def solution_10(n=2000000):
    """ find the sum of primes below two million """ 
    
    total = 0
    for i in xrange(n):
        if is_prime(i):
            total +=i
    return total


def solution_1(n=1000):
    total = 0
    for i in xrange(n):
        if i%3 == 0 or i%5==0:
            total += i
    return total 



def solution_2(n=4000000):
    # need to not only cache the fibonacci sequence, but also only sum up the even numbered ones
    fib=1
    x= 1
    y=0
    total = 0
    for i in xrange(1,n):
        if i==1:
            y+=1            
            fib=1
            continue 
        fib = x + y
        y = x
        x = fib 
        if fib%2==0:
            total += fib 
        if i%1000==0:
            print(i)    
    return total 

        