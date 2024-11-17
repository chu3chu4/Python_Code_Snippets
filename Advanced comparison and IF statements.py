age = 19
height = 140

if height < 100:
    print("you can't ride the ride")
elif height < 150:
    print("you can ride the first ride ")
elif height < 200:
    print("you can ride the 2nd ride")

if age > 10 and height > 150:
    print ("you can ride all the rides")


if age > 10 and height > 150 or age > 18:
    print("you can ride the 3rd ride")