# Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321.
# The program should then print out the number of times the user tried different codes.

# attempts = 1
# while True:
#     pin = input("PIN: ")
#     if pin == "4321":
#         break
#     print("Wrong")
#     attempts += 1
 
# if attempts == 1:
#     print("Correct! It only took you one single attempt!")
# else:
#     print(f"Correct! It took you {attempts} attempts")
    

# Please write a program which keeps asking the user for words. If the user types in end, 
# the program should print out the story the words formed, and finish.
# Change the program so that the loop ends also
# if the user types in the same word twice in a row.

# result =""
# prev=""
# while True:
#     word = input("Please type in a word: ")
#     if word == "end" or word ==prev:
#         break
#     result+=" " + word
#     prev=word
        
    
# print(result)

# Please write a program which asks the user for integer numbers. 
# The program should keep asking for numbers until the user types in zero.
# count =0
# sum=0
# positive=0
# neagtive=0

# while True:
#     number = int(input("Number: "))
#     if number==0:
#         break
    
#     count +=1
#     sum += number
#     mean = sum/count
    
#     if number > 0:
#         positive +=1
    
#     elif number<0:
#         neagtive += 1

    
# print(f"Numbers typed in {count}")
# print(f"The sum of the numbers is {sum}")
# print(f"The mean of the numbers is {mean}")
# print(f"Positive numbers {positive}")
# print(f"Negative numbers {neagtive}")


# i = 2

# while i<=30:
#     if i%2==0:
#         print(i)
        
#     i+=1
    
# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while number >=1:
#     print(number)
#     number-=1
# print("Now!")

# test=1
# user = int(input("Upper limit: "))

# while test<user :
#     print(test)
#     test+=1

