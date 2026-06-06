# Seconds to minutes and format converter.
seconds=int(input("Enter time (in seconds)= "))
minutes=seconds//60 #gives 16
secondsleft=seconds-(minutes*60)
               #that .66 to be multiplied by 60. how to get .66?yes remainder.
print("time is",minutes,"minutes",secondsleft,"seconds")
# Somebody enters 1000 seconds so 1000//60= 16 (16.67)

# practically 16 minutes= 16x60=960.
