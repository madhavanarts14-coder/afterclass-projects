print("classroom points calculator\n")
#stores points earned by 5 classroom teams
team1 = 120
team2 = 95
team3 = 140
team4 = 110
team5 = 85

#calculates the total and average points
total = team1+team2+team3+team4+team5
average = total/5
print("total points: ", total )
print("average points per team: ", average, "\n")

#calculates total rewaard stars
stars_per_point = 2
reward_stars = stars_per_point*total
print("total reward stars: ", reward_stars)

#calculates total boxes needed for reward stars and leftovers
box_capacity = 25
boxes_used = reward_stars//box_capacity
leftover = reward_stars%box_capacity
print("full boxes packed: ", boxes_used)
print("leftover : ", leftover,"\n")

#compares the last week's total points with the current week
last_week = 500
print("better than last week? : ", total>last_week)
print("same as last week? : ", total==last_week)
print("atleast as good as last week? : ", total>=last_week, "\n")

#changes the total from the bonus points and and the reduced points
bonus_points = 30
total += bonus_points
print("points after bonus: ", total)
missed_task = 15
total -= missed_task
print("points after missed task: ", total, "\n" )

#calculates the final reward stars and boxes needed
reward_stars = stars_per_point*total
boxes_used = reward_stars//box_capacity
leftover_boxes = reward_stars%box_capacity
print("final boxes packed: ", boxes_used)
print(" final leftover boxes: ", leftover_boxes)

 



