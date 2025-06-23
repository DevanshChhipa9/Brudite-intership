
#* Write a program in Python to perform the following operation:        
# If a number is divisible by 3 it should print “SKILLBREW” as a string
#  If a number is divisible by 5 it should print “BRUDITE” as a  string
#  If a number is divisible by both 3 and 5 it should print
#  “BRUDITE - NIRVANA” as a string 

#? Question_1 
"""
?num = int(input("ENTER THE Number:-"))
?if num % 3 == 0 and num % 5 == 0:
 ?  print("Brudite - Nirvana") 
?elif num % 3 == 0:
 ?  print("SKILLBREW")
?elif num % 5 == 0:
 ?  print("BRUDITE")
?else:
 ?  print("Number is not divisible by 3 and 5 ")

"""
#*  Write a program that accepts a string as input from
#  the user and calculates the number of digits and
#  letters.
#      Input: Hello123 
#      Output: Alphabets: 5 & Number : 3  
# * Question 2
''' 
user = input("Enter a string:-")
letterCount = 0
digitCount = 0

for char in user:
  if char.isalpha():  
      letter_count += 1
  elif char.isdigit():  
       digit_count += 1

print("Alphabets:", letter_count, "& Number :", digit_count)
'''
#* Write a Python program to input marks for five
 #subjects Physics, Chemistry, Biology, Mathematics,and Computer. Calculate the percentage and grade
 #according to the following:
 #Percentage >= 90% : Grade A
 #Percentage >= 80% : Grade B
 #Percentage >= 70% : Grade C
 #Percentage >= 60% : Grade D
 #Percentage >= 40% : Grade E
 #Percentage < 40% : Grade F
#! Question 3 
"""
#!Physics = 38
#!Chemistry = 95
#!Biology = 87
#!Mathematics = 59
#!Computer = 90

#!percentage = ((Physics + Chemistry + Biology + Mathematics + Computer) / 500) * 100

#!if percentage >= 90 and percentage <= 100:
  print("Grade A")
#!elif percentage >= 80:
  print("Grade B")
#!elif percentage >= 70:
  print("Grade C")
#!elif percentage >= 60:
  print("Grade D")
#!elif percentage >= 40:
  print("Grade E")
#!elif percentage < 40 and percentage > 0:
  print("Grade F")

"""

#*Write a Python program to find the sum of all odd numbers between two given numbers. 
 #Start = 1, stop = 10
  #Sum of odd numbers: 25

#todo Question 4
"""
todo start = 5
todo stop = 10
todo sumOdds = 0

todo for num in range(start, stop + 1):
todo   if num % 2 != 0:  
todo      sumOdds += num 
todo print("Sum of odd numbers:", sumOdds) 

"""
#*  Write a Python program to find the factorial of a number using a for loop.

#? Question 5
"""
num = int(input("Enter a number: "))
factorial = 1

if num == 0 or num == 1:
   factorial = 1
else:
  for i in range(2, num + 1):
      factorial *= i 
print("Factorial of", num, "is", factorial)
"""

#* Write a Python program to check if a given number is a perfect number. 
#A Perfect number is a positive integer that is equal to the sum of its proper divisors. For instance, 6 has divisors 1, 2,and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.
  # Input: 5 
  # Output: No

  #* Question 6
"""
num = int(input("Enter a number: "))
sumOfDivisors = 0

for i in range(1, num):
  if num % i == 0:  
     sumOfDivisors += i  
if sumOfDivisors == num:
    print("Yes, it is a Perfect Number.")
else:
    print("No, it is not a Perfect Number.")
"""

#* Write a Python program to check if a string is an anagram of another string.
   #string1 = "listen", string2 = "silent"
   #Output: True
#! Question 7
"""
!str1 = input("Enter first word: ")
!str2 = input("Enter second word: ")

!if sorted(str1) == sorted(str2):
   print("True")
!else:
    print("False")
"""

#* Write a Python program to calculate the LCM (Least Common Multiple) of two numbers.
  #number1 = 12, number2 = 18
    #LCM of 12 and 18 are: 36

#todo Question 8
"""
todo num1 = int(input("Enter first number: "))
todo num2 = int(input("Enter second number: "))

todo if num1 > num2:
    greater = num1
todo else:
    greater = num2

todo while True:
 todo if (greater % num1 == 0) and (greater % num2 == 0):
        print("LCM of", num1, "and", num2, "is:", greater)
 todo        break
 greater += 1
"""

#* Write a Python program to count the frequency of each element in a list.
  #Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
    #Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
 #? Question 9
"""
?input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
?frequency = {}

?for item in input_list:
 ?   if item in frequency:
  ?      frequency[item] += 1
   ? else:
    ?    frequency[item] = 1  
? print("Frequency count:", frequency)
"""

#*Write a Python program to reverse the order of words in a given sentence.
  #Input_sentence = “Hello, World! Welcome to Python programming.”
    # Output after reverse = “programming. Python to Welcome World! Hello,”
 #* Question 10

"""
input_sentence = "Hello, World! Welcome to Python programming."
words = input_sentence.split()

reversed_words = words[::-1]
reversed_sentence = ' '.join(reversed_words)
print("Output after reverse =", reversed_sentence)
""" 

#*Write a Python program to calculate the sum ofdigits of a given number until the sum becomes a single-digit number.
  # Sample Input: num = 987
  # Sample Output: Sum_of_digits = 24,
  # Again compute the sum of digits so that it can be reduced to on single digit.
  # Final Output: 6

#! Question 11
"""
num = int(input("Enter a number: "))
def sumOfDigits(n):
    total = 0
    while n > 0:
        digit = n % 10      
        total += digit       
        n = n // 10          
    return total

while num >= 10:
    num = sumOfDigits(num)
    print("Intermediate Sum:", num)
print("Final Output:", num)
"""

#* Write a Python program to reverse a number using a while loop.
  # Sample Input: num = 12345
    #Sample Output: revnum = 54321
#todo Question 12
"""
num = int(input("Enter a number: "))

revnum = 0

while num > 0:
    last_digit = num % 10
    revnum = revnum * 10 + last_digit
    num = num // 10

print("Reversed number =", revnum)
"""