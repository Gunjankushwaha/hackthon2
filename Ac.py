case=input("enter thr letter")
if case in("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"):
    print("upper cese")
else:
    print("lower case")































 
# letter=input("enter the letter:-")
# if letter>="a" or letter<="z":
#     special_character=input("enter the special_character:-")
#     if special_character=="@" or "#" or "$":
#         number=int(input("enter the number:-"))
#         if number>=1:
#             print(letter+special_character+str(number))
#         else:
#             print("not strong_password")
#             # ("it is not a number")
#     else:
#         print("it is not charecter") 
# else:
#     print("not strong_password")
#     # print("it is not a letter")







letter=input("enter the letter:-")
if letter>="a" and letter<="z":
    # print("it is  letter")
    special_character=input("enter the special_character:-")
    if special_character=="@" or "#" or "$":
        # print("right")
        number=int(input("enter the number:-"))
        if number>=1:
            # print("right number")
            print(letter+special_character+str(number))
        else:
            print("it is not special_characte")
            # print("not right number")
            # print("wrong letter+special_character+str(number)")
    else:
        print("not special_character")
        # print("not right number")
        # print("it is not special_characte")
else:
    print("not right letter")        
        
                           


             






# num1=int(input("enter the number"))
# num2=int(input("enter the number"))
# symbols=input("enter the symbols")
# if symbols=="+":
#     print(num1+num2)
# elif symbols=="-": 
#     print(num1-num2)
# elif symbols=="*":
#     print(num1%num2)
# elif symbols=="/":
#     print(num1/num2)
# elif symbols=="//":
#     print(num1//num2) 
# elif symbols=="**":
#     print(num1**num2) 
# else:
#     print("ok")                  


    