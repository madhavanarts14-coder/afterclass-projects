print("================================")
print("Daily activity planner")
print("================================\n")

# Ask for the homework time in minutes.
homework_time = input("How much time you need to do homework in ? (minutes): ")
homework_time = int(homework_time)

# decides if the time for homework is short or long
if homework_time > 60:
    plan = "start homework now"
    print ("\nthis is a long homework session\n ", plan, "\n")
else:
    plan = "finish homework quickly"
    print("\nthis is a small homework session,", plan, "\n")

#reminds to pick a hobby if you have free time after homework
free_time = input("is there any free time after homework? (yes/no) :  ")
if free_time == "yes":
    print("reminder: pick a hobby for your free time! \n")

# Print the homework minutes, the plan and the free time answer.
print("========= DAILY PLAN =========\n")
print("homework minutes: ", homework_time)
print("plan: ", plan)
print("free time? : ", free_time)