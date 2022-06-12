from math import trunc
from random import randint
score = 0
numWrong = 0

def titleScreen():
    choice = input("Hello! Do you want to figure out the amount of calories you should be eating to maintain your body weight? (Y/N)")
    if choice == "Y":
        estimateCalories()


def estimateCalories():
    global activityLevel
    global weight
    global height
    global age
    global calories
    print("------------------------------------------------------------------")
    genderInp = input("First, are you a male or female? \n 1) Male \n 2) Female")
    if genderInp == "1":
        isMale = True
    else:
        isMale = False
    print("------------------------------------------------------------------")

    age = input("Second, how old are you?")
    print("------------------------------------------------------------------")
    weight = input("Third, how much do you weigh? (Please answer in pounds)")
    print("------------------------------------------------------------------")
    height = input("Fourth, how tall are you? (Please answer in inches)")
    print("------------------------------------------------------------------")
    activityLevelInp = input("Last Question. About how active are you in a given week? \n 1) No exercise \n 2) Lightly active \n 3) Moderately active \n 4) Very active \n 5) Extremly active")
    if activityLevelInp == "1":
        activityLevel = 1.2
    elif activityLevelInp == "2":
        activityLevel = 1.375
    elif activityLevelInp == "3":
        activityLevel = 1.55
    elif activityLevelInp == "4":
        activityLevel = 1.725
    elif activityLevelInp == "5":
        activityLevel = 1.9
    print("------------------------------------------------------------------")
    if isMale:
        calories = ( 66 + (6.3 * int(weight)) + (12.9 * int(height)) - (6.8 * int(age)) ) * activityLevel
        round(calories, 2)
        print("You should eat approximately " + str(calories) + " calories a day to maintain your body weight")
    else:
        calories = (655 + (4.3 * int(weight)) + (4.7 * int(height)) - (4.7 * int(age)) ) * activityLevel
        round(calories, 2)
        print("You should eat approximately " + str(calories) + " calories a day to maintain your body weight")

titleScreen()

