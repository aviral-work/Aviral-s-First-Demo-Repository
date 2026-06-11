#How to make a Weekly time planner.
sleep=int(input("How many hours you sleep daily= "))
if sleep>24:
    print("You can't sleep more than 24 hours a day.")
food=int(input("Does it takes you how many hours for \n breakfast lunch dinner\n 3? 4? 2? enter that."))
rest=int(input("Enter your rest hour on day= "))
working_block=int(input("Enter your first working block hours= "))
mid_block=int(input("Enter your mid working block hours= "))
end_block=int(input("Enter your last working block hours= "))
weeklysleep=7*sleep
foodtime=food*7
restt=rest*7
working=(working_block+mid_block+end_block)*7
hoursleft=168-(weeklysleep+foodtime+restt+working)
print("You would spend", weeklysleep,"on sleep", foodtime, "on food and" , working , "on working and being productive and with", hoursleft, "of unplanned hours.")
#Make it more interactive and ask the user to input their activities for the unplanned hours.
activities=input("What activities do you want to do with your unplanned hours? ")
print("You have", hoursleft, "hours left for", activities, "each week.")