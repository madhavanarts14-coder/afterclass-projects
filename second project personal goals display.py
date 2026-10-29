#prints title and leaves one line
print("personal goals display: \n")
#import the keyword module
import keyword
#ask three questions
person_name = input("enter your name: ")
goal_name =  input("enter one skill you want to get better at: ")
target_month = input ("enter the month you want to reach it by:")
#store the value 30 for 30 minutes of practise everyday
daily_minutes = 30
#prints goal plan and leaves 1 line above and below
print("\n My personal goal plan \n")
#prints the four plan lines input collected from user
print("name:", person_name)
print("goal:", goal_name)
print("target month:", target_month)
print("daily practise:", daily_minutes, "minutes")
# 2 lines that join using end function
print("status:", end = " ")
print("not started")
print("reminder:", end = " - ")
print("practise every day!")
#prints all the data of the goal plan and prints it in one single line
print("\n In one sentence")
print(person_name, "has planned to work on", goal_name, "for", daily_minutes, "minutes everyday until", target_month )
#prints the reserved keywords lis in Python
print("\n Words Python has reserved for itself: \n")
print(keyword.kwlist)
