userReply=input("Do you want to ship the package (yes / no): ")

if userReply=="yes":
    print("We can help you to do that")
else:
    print("Please feel free to come back later")

customerReply=input("Would you like to buy stamp, envelope, or make copies?")
if customerReply=="stamp":
    print("We have varoius stamp style and size")
elif customerReply=="envelope":
    print("Try our best seller envelope")
elif customerReply=="copy":
    copies=input("How many copies do you need (enter a number): ")
    print("You order {} copies".format(copies) )
else:
    print("Thank you, please come again")