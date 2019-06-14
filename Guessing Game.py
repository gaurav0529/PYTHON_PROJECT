# Loterry Game
print("__________________________________________________________________________")
print("\t\t\tKon Banega CROREPATI")
print("Enter your Name")
a=str(input())
print("\n\n\t\tWelcome to Kon Banega CROREPATI Game",a)
print("About Game\n-->You Have 3 Chances to play.\n-->You have to write any number from 0 to 50.\n-->If your Number Match(same) then you WON THE GAME otherwise You became LOSER.\n\t\tThat's all....")
print("Lets Start The Game",a)
for n in range(1,4):
    print("Chance",n)
    print("ENTER NUMBER 0 TO 50")
    b=int(input())
    import random 
    r=random.randint(0,50)
    print("LOTTERY NUMBER IS",r)
    if r<b:
        print("YOUR NUMBER IS LESS THAN LOTTERY NO.\n\t\t LOSER\n\n")
    elif r>b:
        print("YOUR NUMBER IS HIGHER THAN LOTTERY NO.\n\t\t LOSER\n\n")
    elif r==b:
        print("\t\t\tYou WON THE GAME",a)
        print("\t\tCONGRATULATION YOU BECAME THE ROADPATI Not CROREPATI")
        break
    else:
        print("Something went wrong Please try next time")
print("ThankQ Visit Next Time Again")
