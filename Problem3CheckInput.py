#Miguel Rodriguez
#March 18,2021
#CSS 225 Lab Activity 7
#while the user input gives you a letter between A,B, or C loop will give you Invalid Input

user_input = input("Give me a leter between A,B,or C").upper()
while user_input !='A' and user_input != 'B' and user_input != 'C':
    user_input=input("Invalid Input")
