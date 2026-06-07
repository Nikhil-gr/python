# number = int(input("Please type in a number: "))

# if number >= 100:
#     print("The number was greater than one hundred")
#     number - 100
#     print("Now its value has decreased by one hundred")
#     print(f"Its value is now  {number}")
    
# print(f"{number} must be my lucky number!")
# print("Have a nice day!")

# user = float(input("floating number: "))
# integer = int(user)
# dec = user-integer
# print("Integer part : ", integer)
# print(f"Decimal Part: {dec:.2f}")

# name = "Tim Tester"
# age = 20
# skill1 = "python"
# level1 = "beginner"
# skill2 = "java"
# level2 = "veteran"
# skill3 = "programming"
# level3 = "semiprofessional"
# lower = 2000
# upper = 3000

# print(f"my name is {name} I am {age} years old")
# print("my skills are")
# print(f"- {skill1} {level1}")
# print(f"- {skill2} {level2}")
# print(f"- {skill3} {level3}")
# print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

# print(5, end="")
# print(" + ", end="")
# print(8,end="")
# print(" - ",end="")
# print(4,end="")
# print(" = ",end="")
# print(5 + 8 - 4)

# user = int(input("input a number: "))
# multiple = user * 5

# print(f"{user} times 5 is {multiple}")

# user = int(input("How many days? "))

# seconds = 60 * 60 * 24

# print("Seconds in that many days: ", user * seconds)

# number1 = int(input("Number 1: "))
# number2 = int(input("Number 2: "))
# number3 = int(input("Number 3: "))
# number4 = int(input("Number 4: "))


# sum = number1 + number2 +number3 +number4
# mean = sum / 4
# print(f"The sum of the numbers is {sum} and the mean is {mean}")


# user = float(input("How many times a week do you eat at the student cafeteria? "))
# lunch = float(input("The price of a typical student lunch? "))
# grocery = float(input("How much money do you spend on groceries in a week? "))

# total = (user * lunch) + grocery
# daily = total / 7

# print("Average food expenditure:")
# print("Daily:", daily)
# print("Weekly:", total)

# user = int(input("How many students on the course?"))
# size = int(input("Desired group size?"))

# groups = user //size

# if user % size !=0:
#     groups += 1

# print("Number of groups formed: ", groups)


# user = int(input("Please type in a temperature (F): "))

# celsius = (user - 32) * 5/9

# print(f"{user} degrees Fahrenheit equals to {celsius} degrees Celsius")
# if celsius < 0:

#     print("Brr! It's cold in here!")



# wage = float(input("Hourly wage: "))
# worked = float(input("Hours worked: "))
# day = input("Day of the week: ")

# if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Friday' or day == 'Saturday':
#     total = wage * worked
#     print(f"Daily wages: {total} euros")

# elif day == "Sunday":
#     total = 2*wage*worked
#     print(f"Daily wages: {total} euros")


# points = int(input("How many points are on your card? "))

# if points < 100:
#     print("Your bonus is 10%")
#     bonus = points+ (points * 0.1)
# else:
#     print("Your bonus is 15%")
#     bonus = points+ (points * 0.15)

# print("What is the weather forecast for tomorrow?")
# temperature = float(input("Temperature: "))
# rains = input("will it rain(yes/no): ")


# if temperature > 20:
#     print("Wear jeans and a Tshirt")
    
# elif temperature > 10 and temperature <=20:
#     print("Wear jeans and a Tshirt")
#     print("I recommend a jumper as well")

# elif temperature > 5 and temperature <=10:
#     print("Wear jeans and a Tshirt")
#     print("I recommend a jumper as well")
#     print("Take a jacket with you")

# elif temperature <= 5:
#     print("Wear jeans and a Tshirt")
#     print("I recommend a jumper as well")
#     print("Take a jacket with you")
#     print("Make it a warm coat, actually")
#     print("I think gloves are in order")


# if rains == 'yes':
#     print("Don't forget your umbrella!")


# print("Person 1: ")
# Name1 = input("Name: ")
# Age1 = int(input("Age: "))
# print("Person 2: ")
# Name2 = input("Name: ")
# Age2 = int(input("Age: "))


# if Age1 > Age2:
#     print(f"The elder is {Name1}")
# elif Age1 < Age2:
#         print(f"The elder is {Name2}")
# elif Age1 == Age2:
#     print(f"{Name1} and {Name2} are the same age")


# firstWord = input("Please type in the 1st word: ")
# secondWord = input("Please type in the 2nd word: ")


# if (firstWord) < (secondWord):
#     print(f"{secondWord} comes alphabetically last.")
# elif firstWord== secondWord:
#     print("You gave the same word twice.")

# else:
#     print(f"{firstWord} comes alphabetically last.")


# marks = int(input("How many points[0-100]: "))

# if marks > 100:
#     print("impossible!")
# elif marks >= 90 and marks <100:
#     print("Grade: 5")
# elif marks >= 80 and marks <90:
#     print("Grade: 4")
# elif marks >= 70 and marks <80:
#     print("Grade: 3")
# elif marks >= 60 and marks < 70:
#     print("Grade: 2")
# elif marks >= 50 and marks <60:
#     print("Grade: 1")
# elif marks >= 0 and marks < 50:
#     print("Grade: fail")
# else:
#     print("impossible!")


# giftPrice = float(input("Value of gift: "))

# if giftPrice >=5000 and giftPrice<=25000:
#     tax = (100 + (giftPrice-5000) * 0.08)
#     print(f"Amount of tax: {tax} euros")

# elif giftPrice >=25000 and giftPrice<=55000:
#     tax = (1700 + (giftPrice-25000) * 0.1)
#     print(f"Amount of tax: {tax} euros")
    
# elif giftPrice >=55000 and giftPrice<=200000:
#     tax = (4700 + (giftPrice-55000) * 0.12)
#     print(f"Amount of tax: {tax} euros")
    
# elif giftPrice >=200000 and giftPrice<=1000000:
#     tax = (22100 + (giftPrice-200000) * 0.15)
#     print(f"Amount of tax: {tax} euros")

# elif giftPrice >=1000000:
#     tax = (142100 + (giftPrice-1000000) * 0.17)
#     print(f"Amount of tax: {tax} euros")
# else: 
#     print("No tax!")


# while True:
#     print("hi")
#     question = input("Shall we continue?")
#     if question =="no":
#         break
# print("okay then")

# number = 5
# print("Countdown!")

# while True:
#   print(number)
#   number = number - 1
#   if number < 0:
#     break

# print("Now!")


