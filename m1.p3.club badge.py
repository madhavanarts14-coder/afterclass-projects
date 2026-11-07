print("\n School club member badge \n")

#asks for input from user for their name and club name
MEMBERname = input("enter your name: ")
CLUBname = input ("enter which club you are in: ")
MemberNUMBER = 8
Points = 9.5
is_active = True

#prints the member details and their data types
print("\nMember number: ", MemberNUMBER, end =" -> ")
print(type(MemberNUMBER))
print("\npoints: ",Points, end =" -> ")
print(type(Points))
print("\nActive: ", is_active, end =" -> ")
print(type(is_active))

#creates a badge code for the member with the first 3 letters of their name, the last letter of their club name, and their Member number 
name3letters = MEMBERname[0:3]
lastLETTERclub = CLUBname[-1]
MemeberNUMBER2 = str(MemberNUMBER)
badge_code = name3letters + lastLETTERclub + MemeberNUMBER2
print("\nBadge code is", badge_code)

#prints the final school club badge
print("\n ======== CLUB BADGE ======== \n ")
print("Member: " + MEMBERname)
print("club: " + CLUBname)
print("Badge code: " + badge_code)
print("points: " + str(Points) + " | " "Active: " + str(is_active))


