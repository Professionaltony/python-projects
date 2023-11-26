print("General Knowledge quiz!")

playing = input("Are you ready to play? ")

if playing.lower() != "yes":
    quit()

print("Game on!")
score = 0

answer = input("Which planet has the most moons? ")
if answer.lower() == "saturn":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("What country drinks the most coffee per capita? ")
if answer.lower() == "finland":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("What country has the highest life expectancy? ")
if answer.lower() == "hong kong":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("Aureolin is a shade of what color? ")
if answer.lower() == "yellow":
    print("correct")
    score += 1
else:
    print("incorrect")

  

print("You recieved a score of " + str(score) +"!")
print("You got " + str((score/4) * 100) + "% correct!")
