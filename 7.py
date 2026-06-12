# def line(num, char):
#     if char == "":
#         print("*" * num)
#     else:
#         print(num*char[0])
    
# if __name__ == "__main__":
#     line(3, "")



# def box_of_hashes(height):
#     count =0
#     while count<height:
        
#         print(10 * "#")
#         count+=1

# if __name__ == "__main__":
#     box_of_hashes(2)

# def line(length, char):
#     print(length * char)

# def box_of_hashes(height):
#     while height>0:
#         line(10, "#")
#         height-=1

# if __name__ == "__main__":
#     box_of_hashes(5)




# def greatest_number(num1, num2, num3):
#     if num1>=num2 and num1>=num3:
#         return num1
#     elif num2>=num3 and num2>=num1:
#         return num2
#     elif num3>=num1 and num3>=num2:
#         return num3

# here there will be case where we have to make sure the
# program will choose greatest number despite the presence of 
# negative value. so using >= will avoid error which u will get
# if u dont use it when testing the code
    
# if __name__ == "__main__":
#     greatest = greatest_number(5, 4, 8)
#     print(greatest)


# def same_chars(char, num1, num2):
#     if num1>=len(char) or num2 >= len(char):
#         return False
    
#     return char[num1] == char[num2]
    
    
# if __name__ == "__main__":
#     print(same_chars("programmer", 6, 7)) 
