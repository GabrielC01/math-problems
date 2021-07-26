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

#8 Largest product in a series
def largestProductInSeries():
    print('The thirteen adjacent numbers that have the greatest product')
    greatNumber="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    selStart = 0
    selEnd = 3
    largestProduct = 0
    digits = ""
    while selEnd < len(greatNumber):
        product = 1
        tmpDigits = ""
        for i in range(selStart, selEnd + 1):
            product *= int(greatNumber[i])
            tmpDigits += greatNumber[i]
        if product > largestProduct:
            largestProduct = product
            digits = tmpDigits
        selEnd += 1
        selStart += 1
    print('--> Digits: ' + digits + '\t Product: ' + str(largestProduct))

# RUN FUNCTIONS INDIVIDUALLY FROM THIS FILE
try:
    function = sys.argv[1]
    globals()[function]()
except IndexError:
    raise Exception("You need to provide a function.")
except KeyError:
    raise Exception("Function {} hasn't been found".format(function))
