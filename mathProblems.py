#           Math problems 
# Author:   Gabriel Costa Chaves

import sys      # Used for calling functions individually from program arguments
                # The code for this is at the end of this file

def reverseStr(str):
    return str[::-1]

## FUNCTIONS ##

#1 Multiples of 3 or 5
def threeAndFiveMultiples():
    print('Sum of all the multiples of 3 or 5 below 1000.')
    s = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    print('--> ' + str(s))

#2 Even Fibonacci numbers
def evenFiboNumbers():
    print('The sum of even-valued fibonacci terms, only those whose values don\'t exceed four million')
    prevNum = 1
    currNum = 2
    result  = 2
    while currNum <= (10**6)*4:
        nextNum = prevNum + currNum
        prevNum = currNum
        currNum = nextNum
        if currNum % 2 == 0:
            result += currNum
    print('--> ' + str(result))

#3 Largest prime factor
def largestPrimeFactor():
    print('The largest prime factor of the number 600851475143')
    # We can't divide a number evenly by more than its half
    givenNum = 600851475143
    largestPrime = 0
    for factor in range(1, givenNum):
        if factor >= round(givenNum / 2):
            break
        if givenNum % factor == 0:
            for i in range(1, factor):
                if factor % i != 0 and i == factor - 1:
                    largestPrime = factor
    print('--> ' + str(largestPrime))

#4 Largest palindrome product
def largestPalindrome():
    print('The largest palindrome made from the product of two 3-digit numbers')
    largestPalindrome = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            if str(x * y) == reverseStr(str(x * y)):
                if x * y > largestPalindrome:
                    largestPalindrome = x * y
    print('--> ' + str(largestPalindrome))

#5 Smallest multiple
def smallestMultiple():
    numFactors = 20
    n = 10
    while True:
        found = False
        for i in range(1, numFactors+1):
            if n % i != 0:
                found = False
                break
            else:
                found = True
        if found:
            print('--> ' + str(n))
            return
        n += 1

#6 Sum square difference
def sumSquareDiff():
    print('The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum')
    sumOfSquare = 0
    squareOfSum = 0
    for n in range(1, 101):
        sumOfSquare += n**2
        squareOfSum += n
    squareOfSum = squareOfSum**2
    print('--> ' + str(squareOfSum - sumOfSquare))

#7 10001st prime
def tenThousandFirstPrime():
    print('The 10001st prime number')
    n = 1
    index = 1
    while True:
        for i in range(2, n):
            if n % i == 0:
                break
            elif i == n - 1 and n % i != 0:
                index += 1
            if index == 10001:
                print('--> ' + str(n))
                return
        n += 1

# RUN FUNCTIONS INDIVIDUALLY FROM THIS FILE
try:
    function = sys.argv[1]
    globals()[function]()
except IndexError:
    raise Exception("Please provide function name")
except KeyError:
    raise Exception("Function {} hasn't been found".format(function))
