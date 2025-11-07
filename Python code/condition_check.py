
# # Task One

# age = int(input("Enter your age: "))

# if age < 13:
#     print("Child")
# elif age <= 19:
#     print("Teenager")
# else:
#     print("Adult")


# # Task Two

# any_digit = int(input("Enter your digit"))

# if any_digit % 2 ==0:
#     print("Even")

#     if any_digit > 0:
#         print("Positive")

#     elif any_digit < 0:
#         print("Negetive")
#     else:
#         print("Zero")

# else:
#     print("Odd")

# task 3 



"""
any_digit = int(input("Enter your digit: "))

# Even or Odd check
if any_digit % 2 == 0:
    print("Even")
else:
    print("Odd")

# Positive, Negative or Zero check
if any_digit > 0:
    print("Positive")
elif any_digit < 0:
    print("Negative")
else:
    print("Zero")

"""



# a = int(input("Enter the First number: "))
# b = int(input("Enter the Second number: "))
# c = int(input("Enter the Third number: "))

# if a>b and a>c:
#     print("a is largest: ", a)

# elif b>a and b>c:
#     print("b is largest: ", b)

# else:
#     print("c is largest c: ", c)


# # Tast 3    

# number1 = int(input("Enter a first number: "))
# number2 = int(input("Enter a second number: "))

# if number1> number2:
#     print(number1," is largest")
# else:
#     print(number2," is largest number")

# #5: Leap Year Checker

# year  = int(input("Enter the year: "))

# if year % 4 ==0:
#     print("Leap Year")

# elif year % 400 == 0 and year % 100 != 0:
#     print("Leap Year")

# else:
#     print("Not leap year")


"""
year = int(input("Enter the year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
    
"""



# ***************************


# units = int(input("Enter number of units consumed: "))

# if units  <= 100:
#     bill = units *5

# elif units <= 200:
#     bill = units * 7

# else:
#     bill = units * 10

# print("Total paybil amount: ", bill, "BDT")



"""
units  = int(input("Enter number of units consumed: "))

if units <= 100:
    bill = units * 5

elif units <= 200:

    bill = (100 * 5) + ((units - 100)*7)

else:
    bill = (100*5) + (100*7) + ((units - 200)*10)

print("Total payable amount:", bill, "BDT")
"""


#****************************






# # Task 6: Largest of three numbers

# number_1 = int(input("Enter the first number: "))
# number_2 = int(input("Enter the second number: "))
# number_3 = int(input("Enter the third number: "))

# if number_1> number_2 and number_1> number_3:
#     print(number_1, " is the largest number")

# elif number_2>number_1 and number_2> number_3:
#     print(number_2, " is the largest number")

# else:
#     print(number_3, " is the largest number")


# # Task 7: Pass or Fail


# marks = int(input("Enter the marks: "))

# if marks>= 33:
#     print("Pass")

# else:
#     print("Fail")


# # Vowl or Consonent

# letter = input("Enter the letter: ").lower

# if letter in ["a", "e", "i", "o", "u"]:
#     print("Vowel")

# else:
#     print("Consonent")


"""
letter = input("Enter the letter: ").lower()

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Vowel")
else:
    print("Consonant")
"""


# # task 9 Temperature 9

# temperature = int(input("Enter the temperature: "))

# if temperature >= 30:
#     print("Hot day")

# elif temperature >=20 and temperature <= 29:
#     print("Warm day")
# elif temperature >= 10 and temperature <= 19:
#     print("Cool day")

# else:
#     print("Cold day")


# # Odd or Even & Divisible by 5

# number = int(input("Enter the number: "))

# if number %2 ==0 and number %5 ==0:
#     print("Even and divisible by 5")

# elif number % 2 ==0:
#     print("Even but not divisible by 5")

# else:
#     print("Odd number")


# # Task 11: Even or odd sum

# number1 = int(input("Enter the firs number: "))
# number2 = int(input("Enter the second number: "))

# sum = number1 + number2


# if sum % 2 == 0:
#     print(sum, "The sum is even")

# else:
#     print("Odd")




