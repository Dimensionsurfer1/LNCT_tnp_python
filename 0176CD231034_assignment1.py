'''Name: Aryan Saxena 
Enrollment: 0176CD231034 
Batch: 5 
Batch Time: 10:30 to 12:10 
'''
 
# Conditional statement: 
 
#Q1.  
number = int(input('please enter a number: ')) 

if number > 0 : 

    print('the number is positive') 

elif number < 0 : 

    print('the number is negative') 

elif number == 0 : 

    print('the number is 0') 
 
#Q2. 
number = int(input('please enter a number: ')) 

if number % 2 ==0 : 

    print('the number is even') 

else  : 

    print('the number is odd') 

#Q3. 

number = int(input('please enter a year: ')) 

if number % 400 == 0: 

    print('the year is a leap year') 

elif number % 100 == 0: 

    print('the year is not a leap year') 

elif number % 4 == 0: 

    print('the year is a leap year') 

 

#Q4 
 

number1 = int(input('enter the first number '))  

number2 = int(input('enter the second number ')) 

if number1 > number2: 

    print(number1,' is greater than ', number2) 

else: 

     print(number2,' is greater than ', number1) 

#Q5 

number1 = int(input('enter your age: '))  

if number1 > 18: 

    print('you are eligible to vote') 

else: 

    print('you are not eligible to vote') 

#Q6. 

charachter = str(input('enter a charachter: ')) 

vowels = ('a','e','i','o','u') 

if charachter in vowels: 

    print('the charachter is an vowel') 

else: 

    print('the charachter is not an vowel') 

#Q7 

number = int(input('enter a number: ')) 

if number % 5 ==0: 

    print('the number is divisible by 5') 

else: 

    print('the number is not divisible by 5') 

 

#Q8 

num = int(input("Enter a number: ")) 

if -9 <= num <= 9: 

    print("The number is a single-digit number.") 

elif -99 <= num <= 99: 

    print("The number is a two-digit number.") 

else: 

    print("The number has more than two digits.") 

#Q9 

num = int(input("Enter the marks you gained: ")) 

if num >= 40: 

    print("The student has passed") 

else: 

    print("The student has failed") 

#Q10. 

num = int(input("Enter a number ")) 

if num % 3 ==0 and num % 7 ==0: 

    print("The number is divisible by both 7 and 3") 

else: 

    print("The number is not divisible by either one of 3 and 7 or by both")				 

# Ladder If & Nested If: 

#Q1. 

a = int(input('enter no1 ')) 

b = int(input('enter no2 ')) 

c = int(input('enter no3 ')) 

if a > b and a > c: 

    print(a,' is the largest number out of the three') 

elif b > a and b > c: 

    print(b,' is the largest number out of the three') 

else: 

    print(c,'is the largest number out of the three') 
 

#Q2. 

a = int(input('enter your age ')) 

if a < 13: 

    print('you are a child') 

elif 13<= a <= 19: 

    print('you are a teenager') 

elif 20 <= a <= 59: 

    print('you are an adult') 

elif a > 60: 

    print('you are a senior citizen') 

#Q3 

a = int(input('enter your marks ')) 

if a < 35: 

    print('you have failed') 

elif 35<= a <= 49: 

    print('your grade is D') 

elif 50 <= a <= 74: 

    print('your grade is C') 

elif 75<= a <= 89: 

    print('your grade is B') 

elif 90 <= a <= 100: 

    print('your grade is A') 

 

#Q4. 

a = int(input("Enter side a: ")) 

b = int(input("Enter side b: ")) 

c = int(input("Enter side c: ")) 

  

if a == b == c: 

    print("Equilateral triangle") 

elif a == b or b == c or a == c: 

    print("Isosceles triangle") 

else: 

    print("Scalene triangle") 

#Q5 

ch = input("Enter a character: ") 

  

if ch.isupper(): 

    print("Uppercase letter") 

elif ch.islower(): 

    print("Lowercase letter") 

elif ch.isdigit(): 

    print("Digit") 

else: 

    print("Special symbol") 

#Q6 

units = int(input("Enter units consumed: ")) 

if units <= 100: 
    bill = units * 5 
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7 
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10 

print("Electricity bill = ₹", bill) 

#Q7 

a = int(input("Enter first number: ")) 

b = int(input("Enter second number: ")) 

c = int(input("Enter third number: ")) 

d = int(input("Enter fourth number: ")) 

  

if a > b: 

    if a > c: 

        if a > d: 

            largest = a 

        else: 

            largest = d 

    else: 

        if c > d: 

            largest = c 

        else: 

            largest = d 

else: 

    if b > c: 

        if b > d: 

            largest = b 

        else: 

            largest = d 

    else: 

        if c > d: 

            largest = c 

        else: 

            largest = d 

  

print("Largest number is:", largest) 

#Q8 

year = int(input("Enter a year: ")) 

  

if year % 100 == 0: 

    print("It is a century year") 

else: 

    print("It is not a century year") 

  

# Leap year check 

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0): 

    print("It is also a leap year") 

else: 

    print("It is not a leap year") 

#Q9. 

weight = float(input("Enter weight (kg): "))  

height = float(input("Enter height (m): ")) 

bmi = weight / (height ** 2) 

print("BMI =", round(bmi, 2)) 

if bmi < 18.5:  

    print("Underweight") 

elif 18.5 <= bmi <= 24.9:   

    print("Normal")  

elif  25 <= bmi <= 29.9: 

    print("Overweight")  

else:  

    print("Obese") 

#Q10 

a = int(input("Enter first number: ")) 

b = int(input("Enter second number: ")) 

c = int(input("Enter third number: ")) 

  

if a < b: 

    if a < c: 

        smallest = a 

   

 

    else: 

        smallest = c 

        if b < c: 

            smallest = b 

        else: 

            smallest = c 

  

print("Smallest number is:", smallest) 

# Fort Loops problems: 

# 1. Armstrong Numbers (100-999)
print("--- Problem 1: Armstrong Numbers ---")
for num in range(100, 1000):
    digit_sum = 0
    for digit in str(num):
        digit_sum += int(digit) ** 3
    if digit_sum == num:
        print(num)

# 2. First n Prime Numbers
print("\n--- Problem 2: First n Prime Numbers ---")
n = int(input("Enter how many prime numbers (n): "))
count = 0
num = 2
while count < n:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1
print()

# 3. Numbers Divisible by 3 with Digit Sum <= 10
print("\n--- Problem 3: Special Numbers 1-500 ---")
for num in range(1, 501):
    if num % 3 == 0:
        digit_sum = 0
        for digit in str(num):
            digit_sum += int(digit)
        if digit_sum <= 10:
            print(num, end=" ")
print()

# 4. Star Pyramid
print("\n--- Problem 4: Star Pyramid ---")
h = int(input("Enter height of pyramid: "))
for i in range(h):
    print(" " * (h - i - 1) + "*" * (2 * i + 1))

# 5. Pangram Checker
print("\n--- Problem 5: Pangram Checker ---")
text = input("Enter a string: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True
for char in alphabet:
    if char not in text:
        is_pangram = False
        break
if is_pangram:
    print("It is a Pangram.")
else:
    print("It is NOT a Pangram.")

# 6. Twin Primes (1-100)
print("\n--- Problem 6: Twin Primes ---")
def check_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

for i in range(1, 99):
    if check_prime(i) and check_prime(i + 2):
        print(f"({i}, {i+2})")

# 7. Harshad Number
print("\n--- Problem 7: Harshad Number ---")
num = int(input("Enter a number: "))
digit_sum = 0
for digit in str(num):
    digit_sum += int(digit)
if num % digit_sum == 0:
    print("It is a Harshad number.")
else:
    print("It is NOT a Harshad number.")

# 8. Pascal's Triangle
print("\n--- Problem 8: Pascal's Triangle ---")
rows = int(input("Enter number of rows: "))
triangle = []
for i in range(rows):
    row = [1] * (i + 1)
    if i > 1:
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)
    print(" " * (rows - i), end="")
    for val in row:
        print(val, end=" ")
    print()

# 9. Sum of Series
print("\n--- Problem 9: Sum of Squares Series ---")
lim = int(input("Enter n: "))
total = 0
for i in range(1, lim + 1):
    total += i ** 2
print(f"Sum: {total}")

# 10. Strong Number
print("\n--- Problem 10: Strong Number ---")
s_num = int(input("Enter a number: "))
fact_sum = 0
for digit in str(s_num):
    d = int(digit)
    f = 1
    for i in range(1, d + 1):
        f *= i
    fact_sum += f
if fact_sum == s_num:
    print("It is a Strong number.")
else:
    print("It is NOT a Strong number.")
