print("======swimming pool entry checker======\n")

#asks for 3 user inputs
age = int(input("What is your age? : "))
can_swim = input("can your swim 25 metres (yes/no)?  : ").strip().lower()
adult = input("is there an adult with you? (yes/no) : ")

#checks if there is an error in the input
if can_swim != "yes" and can_swim != "no":
    print("Input error: please answer in yes or no")

if can_swim != "yes" and can_swim != "no":
    print("Input error: please answer in yes or no")

print()
print("====ENTRY DECISION====")
print("-" * 32)

#find the age group of the person
if age < 4:
    age_group = "toddler"
elif age < 12:
    age_group = "child"
elif age < 18:
    age_group = "teen"
else:
    age_group = "adult"
print("\nage group : ", age_group)

#prints the result if the person is allowed in the deep pool or shallow pool
if can_swim == "yes" and adult == "yes":
    print("deep pool : allowed - you can swim and an adult is with you")

if age < 12 or can_swim == "no":
    print("shallow end : stay in the shallow end today")

#prints an safety reminder if an adult is not with you
if not adult == "yes":
    print("reminder: no adult with you - tell the lifeguard")
