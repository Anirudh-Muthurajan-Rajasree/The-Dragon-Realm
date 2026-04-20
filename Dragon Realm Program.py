# This is a simple text-based adventure game called "Dragon Realm"
# The player is a brave adventurer who enters the Dragon Realm and has to choose between two caves, one with a friendly dragon and one with an aggressive dragon. The player has to choose wisely to find the treasure and avoid being eaten by the aggressive dragon.
# The game also has some special cases for players who do not follow instructions or enter certain symbols as their name, which leads to unique outcomes and endings.
#Created by: Anirudh M.R
#Chapter 1: Name Selection
#Imports the time class to create a delay
import time
#Imports the random class to generate random numbers
import random

#Asks the user to enter their name
print("Kindly enter your name:")
#Stores the user's name in a variable called name
name = input()
#If the user does not enter a name, it will assign a default name to the user and print a message
if name.strip() == "":
    print("Since you did not enter a name, your name will be Saturo Gojo King of the jujutsu sorcerers")
    #This is a delay to make the program more dramatic and creates suspence for the user
    time.sleep(1.5)
    print("Sorry your name will be")
    time.sleep(1.5)
    print("The Almighty")
    time.sleep(1.5)
    print("The Undefeatable")
    time.sleep(1.5)
    print("The Unstoppable")
    time.sleep(1.5)
    print("The Invincible")
    time.sleep(1.5)
    print("The One and Only")
    time.sleep(1.5)
    print("BUG MAN the king of the bugs")
    time.sleep(1.5)
    #Changes the name to Bug Man since the user did not enter a name
    name = "Bug Man"
    #In case the user enters a name, it will welcome the user to the Dragon Realm
else:
    print(f"Welcome to the Dragon Realm {name}\n This program is created by Anirudh M.R!")
    time.sleep(1.5)

#Chapter 2: The Adventure Begins (Intoduction)
#This is a introduction method that will introduce the user to the story and the setting of the game
def Introduction():
    print(f"You are a young but a brave adveturer Mr/Mrs {name} who has just entered the Dragon Realm")
    #Using delay" to make the program more dramatic and creates suspence for the user
    time.sleep(1.5)
    print("The Dragon Realm is a place where dragons live and roam freely")
    time.sleep(1.5)
    print("You have heard stories about the Dragon Realm and you have always wanted to explore it")
    time.sleep(1.5)
    print(f"You the great and almighty {name} have finally mustered up the courage to enter the Dragon Realm")
    time.sleep(1.5)
    print("In the Dragon Realm the dragons who live there are very rich and they have a lot of treasures")
    time.sleep(1.5)
    print("There are some dragons who are friendly and will share their treasures with you but there are also some dragons who are aggresive and will try to attack you\n you also don't have any weapons to defend yourself")
    time.sleep(1.5)
    print(f"You have to be careful almighty {name} and make sure to choose the right path to find the treasures and avoid the aggresive dragons")
    time.sleep(1.5)
    print("You found 2 caves in front of you one of them is the cave of the friendly dragon and the other one is the cave of the aggresive dragon")
    time.sleep(1.5)

#Chapter 3: The Cave of the Dragons (Part 1)
#This is a method that will ask the user to choose a cave
def choose_cave():
    #Creates a variable called cave and assigns it an empty string
    cave = ""
    while cave not in ["1", "2"]:
        #Asks the user to choose a cave 
        print("Which cave will you go into? (1 or 2)\n if you don't follow the instructions you will die...")
        #Stores the user's input in the variable called cave
        cave = input()

        #Type 1: If the user did not enter 1 or 2, it will print a message and end the game according to the name of the user
        if cave not in ["1", "2"]:

            #Path 1: If the user name is bug man and did not enter 1 or 2, it will print a special message and end the game
            if name == "Bug Man":
                print(f"Since you did not follow the instrutions {name} the dragon got tired of waiting and...")
                #Using delay" to make the program more dramatic and creates suspence for the user
                time.sleep(1.5)
                print("First roasted you...")
                time.sleep(1.5)
                print("Then toasted you...")
                time.sleep(1.5)
                print("Then posted you...")
                time.sleep(1.5)
                print("And then for the grand finale...")
                time.sleep(1.5)
                print("You got teleported to the BUG REALM!!!")
                time.sleep(1.5)
                print ("Actually that did not happen but you will get the chance to redeem yourself\n but there is a consequence if you try to be clever...")
                #Breaks the loop
                break

            #Path 2: If the user did not enter 1 or 2 and is not bug man, it will print a message and end the game
            else:
                print(f"Since you did not enter properly Mr/Mrs {name} you will face the consequences of your actions\n but you will get the chance to redeem yourself...")
                time.sleep(1.5)
                print("There are 2 different ways of how this will go in both consequence and redemption...")
                break
        
        #Type 2: If the user enters 1 or 2, it will break the loop and return the user's choice
        elif cave in ["1", "2"]:
            break

    return cave

#Chapter 4: The Cave of the Dragons (Part 2)
#This is a method that will check whether the user chose the friendly cave or the aggresive cave
def check_cave(chosen_cave):
    #Pinting the story of the user entering the cave and encountering the dragon
    print("You approach the cave...")
    #Using delay" to make the program more dramatic and creates suspence for the user
    time.sleep(1.5)
    print("It is dark and spooky...")
    time.sleep(1.5)
    print("A large dragon jumps out in front of you!")
    time.sleep(1.5)
    #Creating a random number between 1 and 2 to determine which cave is the friendly cave and storing it in a variable called friendly_cave
    friendly_cave = random.randint(1, 2)

    #Type 1: If the user chose the friendly cave, it will print a message and end the game according to the name of the user
    if chosen_cave == str(friendly_cave):

        #Path 1: name is bug man, it will print a special message and end the game   
        if  name == "Bug Man":
            print("I am a friendly dragon so i will not eat you but i will give you a treasure")
            time.sleep(1.5)
            print("And also as a reward for your bravery i will take you to the!")
            time.sleep(1.5)
            print("Legendary Realm")
            time.sleep(1.5)
            print("The Realm of riches and treasures")
            time.sleep(1.5)
            print("The ruler of all the realms")
            time.sleep(1.5)
            print("The Great!")
            time.sleep(1.5)
            print("BUG REALM!!!!!!!")

        #Path 2: If the user chose the friendly cave and the name is not bug man, it will print a message and end the game
        else:
            print(f"Gives you his treasure! You are rich almighty and undefeatable {name}!")
            time.sleep(1.5)
            print(f"You have conquered the Dragon Realm almighty {name}!")

    #Type 2: If the user chose the aggresive cave, it will print a message and end the game according to the name of the user
    elif chosen_cave != str(friendly_cave):#Note this will work even if the user did not enter 1 or 2 

        #Path 1: If the user chose the aggresive cave and the name is bug man it will print a special message and end the game 
        if name == "Bug Man":
                print(f"Psych you called (chose) the wrong number (cave) on the Dragon phone (realm)...")
                time.sleep(1.5)
                print("First roasted you...")
                time.sleep(1.5)
                print("Then toasted you...")
                time.sleep(1.5)
                print("Then posted you...")
                time.sleep(1.5)
                print("And then...")
                time.sleep(1.5)
                print("GHOSTED YOU!!!")
                print("And then for the grand finale...")
                time.sleep(1.5)
                print("You got teleported to the BUG REALM!!!")
    
        #Path 2: If the user is not bug man chose the aggresive cave, it will print a message and end the game
        else:
            print("The Dragon opens its Jaw")
            time.sleep(1.5)
            print("Gobbles you down in one bite!")

#Chapter 5: The Decision Point (Play Again or Not)
# The Main Game Loop
# This starts the game for the first time
play_again = "yes"

# As long as play_again is "yes", the game will restart from the beginning
while play_again == "yes" or play_again == "y":
    
    #Runs the introduction method
    Introduction()

    # Runs the cave_number method and stores the user's choice in a variable called cave_number
    cave_number = choose_cave()
    
    #Makes sure that the user chose a cave before checking the cave
    check_cave(cave_number)

# After the dragon encounter...
    print("\nDo you want to play again? (yes/no)")
    #Stores the user's input in the variable called play_again and converts it to lowercase and removes any extra spaces
    play_again = input().lower().strip()

    #Type 1: If the user did not follow the rules then the below message will be printed according to the name of the user and the game will end
    if play_again not in ["yes", "y", "no", "n"]:
        #Path 1: If the user name is bug man, then the below message will be printed and the game will end
        if name == "Bug Man":
            print(f"Since you did not enter a proper input {name} this program is going to restart but first...")
            time.sleep(1.5)
            print("Why are you running away from the greatest realm of all time?")
            time.sleep(1.5)
            print("You already got a room in the 5 star bug supreme hotel.")
            time.sleep(1.5)
            print("You have access to the best bug food\n entertainment\n and friends...")
            time.sleep(1.5)
            print("Sukuna personally gave you bug powers just for you...")
            time.sleep(1.5)
            print("You have access to the best bug powers and you can use them to your advantage...")
            time.sleep(1.5)
            print("Saturo Gojo is personally training you...")
            time.sleep(1.5)
            print("You have access to the best bug training facilities...")
            time.sleep(1.5)
            print("Yuji Itadori personally checks your health...")
            time.sleep(1.5)
            print("The jujitsu socerres personally check you so that you don't get rage baited...")
            time.sleep(1.5)
            print("Your bug assistants make sure that you get aura plus...")
            time.sleep(1.5)
            print("You are listening to the top phonk (bug) songs of the year...")
            time.sleep(1.5)
            print("Your aura is near infinte...")
            time.sleep(1.5)
            print("You should enjoy your stay, almighty powerfull Bug Man who has infinte aura.")

        #Path 2: If the user name is a special character, then the below message will be printed and the game will end
        elif any(char in name for char in [".", "!", "?", ";", ":"]):
            print("Since you did not enter a proper input the dragon realm is going to collapse...")
            time.sleep(1.5)
            print("But wait a minute...")
            time.sleep(1.5)
            print(f"This is not a normal special character {name}.")
            time.sleep(1.5)
            print("This is a point of infinity.")
            time.sleep(1.5)
            print("The true Saturo Sukuna.")
            time.sleep(1.5)
            print("The Dragon Realm will remember you as the true Saturo Sukuna")
            time.sleep(1)
            print(f"Final logged hero: {name}")
            time.sleep(1)
            print('Aura Level: "5000" ')
            print("Dragon Realm collpsing in 3.")
            time.sleep(1.5)
            print("Dragon Realm collpsing in 2.")
            time.sleep(1.5)
            print("Dragon Realm collpsing in 1.")
            time.sleep(1.5)
            print("Dragon Realm has collpsed\n Thank you for playing the Dragon Realm\n We hope you enjoyed the adventure and the unique endings based on your choices and name")
            print("Program created by Anirudh M.R")
            break

        #Path 3: If the user name is a number, then the below message will be printed and the game will end
        elif any(char.isdigit() for char in name):
            print("Since you did not enter a proper input the dragon realm is going to collapse...")
            time.sleep(1.5)
            print("But wait a minute...")
            time.sleep(1.5)
            print(f"This is not a normal name {name}.")
            time.sleep(1.5)
            print("These are the coordinates to reach the point of infinity.")
            time.sleep(1.5)
            print("The true Muzan Jackson.")
            time.sleep(1.5)
            print("In his prime he was the most powerful being in the universe and he still is...")
            time.sleep(1.5)
            print("The master at moonwalking along with Kokushibo and Yoriichi")
            time.sleep(1.5)
            print("The Dragon Realm will remember you as the true Muzan Jackson")
            time.sleep(1)
            print(f"Final logged hero: {name}")
            time.sleep(1)
            print('Aura Level: "100000" ')
            time.sleep(1)
            print("Dragon Realm collpsing in 3.")
            time.sleep(1.5)
            print("Dragon Realm collpsing in 2.")
            time.sleep(1.5)
            print("Dragon Realm collpsing in 1.")
            time.sleep(1.5)
            print("Dragon Realm has collpsed\n Thank you for playing the Dragon Realm\n We hope you enjoyed the adventure and the unique endings based on your choices and name")
            print("Program created by Anirudh M.R")
            break

        #Path 4: If the user name is normal, then the below message will be printed and the game will end
        else:
            print("Since you did not enter a proper input the Dragon Realm is now going to colapse.")
            time.sleep(1)
            print("Dragon Realm collpsing in 3.")
            time.sleep(1)
            print("Dragon Realm collpsing in 2.")
            time.sleep(1)
            print("Dragon Realm collpsing in 1.")
            time.sleep(1)
            print("Dragon Realm has collpsed")
            print("Thank you for playing the Dragon Realm\n We hope you enjoyed the adventure and the unique endings based on your choices")
            print("Program created by Anirudh M.R")
            break

        #Type 2: If the user followed the rules and entered no, it will print a message according to the name of the user and end the game
    elif play_again == "no" or play_again == "n":

        #Path 1: If the user (Bug man) enters no, it will print a special message and end the game
        if name == "Bug Man":
            print("Why are you running away from the greatest realm of all time?")
            time.sleep(1.5)
            print("You already got a room in the 5 star bug supreme hotel.")
            time.sleep(1.5)
            print("You have access to the best bug food\n entertainment\n and friends...")
            time.sleep(1.5)
            print("Sukuna personally gave you bug powers just for you...")
            time.sleep(1.5)
            print("You have access to the best bug powers and you can use them to your advantage...")
            time.sleep(1.5)
            print("Saturo Gojo is personally training you...")
            time.sleep(1.5)
            print("You have access to the best bug training facilities...")
            time.sleep(1.5)
            print("Yuji Itadori personally checks your health...")
            time.sleep(1.5)
            print("The jujitsu socerres personally check you so that you don't get rage baited...")
            time.sleep(1.5)
            print("Your bug assistants make sure that you get aura plus...")
            time.sleep(1.5)
            print("You are listening to the top phonk (bug) songs of the year...")
            time.sleep(1.5)
            print("Your aura is near infinte...")
            time.sleep(1.5)
            print("You should enjoy your stay, almighty powerfull Bug Man who has infinte aura.")            
            time.sleep(1)
            print(f"Final logged hero: {name}")
            time.sleep(1)
            print('Aura Level: "Infinite" ')
            time.sleep(1)
            print("Dragon Realm closing in 3.")
            time.sleep(1)
            print("Dragon Realm closing in 2.")
            time.sleep(1)
            print("Dragon Realm closing in 1.")
            time.sleep(1)
            print("Dragon Realm has closed successfully\n Thank you for playing the Dragon Realm\n We hope you enjoyed the adventure and the unique endings based on your choices and name.")
            print("Program created by Anirudh M.R")
            break

        #Path 2: If the user is a special character and enters no, it will print a special message and end the game
        elif any(char in name for char in [".", "!", "?", ";", ":"]):
            print("Wait a minute...")
            time.sleep(1.5)
            print(f"This is not a normal special character {name}.")
            time.sleep(1.5)
            print("This is a point of infinity.")
            time.sleep(1.5)
            print("The true Saturo Sukuna.")
            time.sleep(1.5)
            print("The Dragon Realm will remember you as the true Saturo Sukuna")
            time.sleep(1)
            print(f"Final logged hero: {name}")
            time.sleep(1)
            print('Aura Level: "Infinite" ')
            time.sleep(1)
            print("Dragon Realm closing in 3.")
            time.sleep(1.5)
            print("Dragon Realm closing in 2.")
            time.sleep(1.5)
            print("Dragon Realm closing in 1.")
            time.sleep(1.5)
            print("Dragon Realm has closed successfully\n Thank you for playing the Dragon Realm\n We hope you enjoyed the adventure and the unique endings based on your choices and name..")
            print("Program created by Anirudh M.R")
            break

        #Path 3: If the user is name is a number and enters no, it will print a special message and end the game
        elif any(char.isdigit() for char in name):
            print("Since you did not enter a proper input the dragon realm is going to collapse...")
            time.sleep(1.5)
            print("But wait a minute...")
            time.sleep(1.5)
            print(f"This is not a normal name {name}.")
            time.sleep(1.5)
            print("These are the coordinates to reach the point of infinity.")
            time.sleep(1.5)
            print("The true Muzan Jackson.")
            time.sleep(1.5)
            print("In his prime he was the most powerful being in the universe and he still is...")
            time.sleep(1.5)
            print("The master at moonwalking along with Kokushibo and Yoriichi")
            time.sleep(1.5)
            print("The Dragon Realm will remember you as the true Muzan Jackson")
            time.sleep(1.5)
            print(f"Final logged hero: {name}")
            time.sleep(1)
            print('Aura Level: "Infinite" ')
            time.sleep(1)
            print("Dragon Realm closing in 3.")
            time.sleep(1.5)
            print("Dragon Realm closing in 2.")
            time.sleep(1.5)
            print("Dragon Realm closing in 1.")
            time.sleep(1.5)
            print("Dragon Realm has closed successfully.\n Thank you for playing the Dragon Realm\n We hope you enjoyed the adventure and the unique endings based on your choices and name.")
            print("Program created by Anirudh M.R")
            break

        #Path 4: If the user entered and entered no it will print a message and end the game
        else:
            print(f"Farewell almighty, {name}. The dragons will remember your courage.")
            time.sleep(1.5)
            print(f"They are listening to Empire phonk whenever they think of you!")
            time.sleep(1.5)
            print(f"For them you are the true Satoru Gojo {name}!")
            time.sleep(1.5)
            print("Dragon Realm closing in 3.")
            time.sleep(1)
            print("Dragon Realm closing in 2.")
            time.sleep(1)
            print("Dragon Realm closing in 1.")
            time.sleep(1)
            print("Dragon Realm has closed successfully\n Thank you for playing the Dragon Realm\n We hope you enjoyed the adventure and the unique endings based on your choices and name.")
            print("Program created by Anirudh M.R")
            break
    #Type 3: If the user followed the rules and entered yes, it will print a message according to the characters name and restart the game
    elif play_again == "yes" or play_again == "y":

        #Path 1: If the user is bug man and enters yes, it will print a special message and restart the game
        if name == "Bug Man":
            print(f"Almighty {name} why did you want to leave the bug realm?")
            time.sleep(1.5)
            print("You already got a room in the 5 star bug supreme hotel.")
            time.sleep(1.5)
            print("You have access to the best bug food\n entertainment\n and friends...")
            time.sleep(1.5)
            print("Sukuna personally gave you bug powers just for you...")
            time.sleep(1.5)
            print("You have access to the best bug powers and you can use them to your advantage...")
            time.sleep(1.5)
            print("Saturo Gojo is personally training you...")
            time.sleep(1.5)
            print("You have access to the best bug training facilities...")
            time.sleep(1.5)
            print("Yuji Itadori personally checks your health...")
            time.sleep(1.5)
            print("The jujitsu socerres personally check you so that you don't get rage baited...")
            time.sleep(1.5)
            print("Your bug assistants make sure that you get aura plus...")
            time.sleep(1.5)
            print("You are listening to the top phonk (bug) songs of the year...")
            time.sleep(1.5)
            print("Your aura is near infinte...")
            time.sleep(1.5)
            print("You should enjoy your stay, almighty powerfull Bug Man who has infinte aura.")
            time.sleep(1.5)
            print("Restarting the game in 3...")
            time.sleep(1)
            print("Restarting the game in 2...")
            time.sleep(1)
            print("Restarting the game in 1...")
            time.sleep(1)
            print(f"Welcome back to the Dragon Realm! {name}!")

        #Path 2: If the user is a special character and enters yes, it will print a special message and restart the game
        elif any(char in name for char in [".", "!", "?", ";", ":"]):
            print("Wait a minute...")
            time.sleep(1.5)
            print(f"This is not a normal special character {name}.")
            time.sleep(1.5)
            print("This is a point of infinity.")
            time.sleep(1.5)
            print("The true Saturo Sukuna.")
            time.sleep(1.5)
            print("A Champion like you should not be leaving the Dragon Realm...")
            time.sleep(1.5)
            print("Restarting the game in 3...")
            time.sleep(1)
            print("Restarting the game in 2...")
            time.sleep(1)
            print("Restarting the game in 1...")
            time.sleep(1)
            print(f"Welcome back to the Dragon Realm Champion! {name}!")

            #Path 3: If the user is name is a number and enters yes, it will print a special message and restart the game
        elif any(char.isdigit() for char in name):
            print("But wait a minute...")
            time.sleep(1.5)
            print(f"This is not a normal name {name}.")
            time.sleep(1.5)
            print("These are the coordinates to reach the point of infinity.")
            time.sleep(1.5)
            print("The true Muzan Jackson.")
            time.sleep(1.5)
            print("In his prime he was the most powerful being in the universe and he still is...")
            time.sleep(1.5)
            print("The master at moonwalking along with Kokushibo and Yoriichi")
            time.sleep(1.5)
            print(f"A true legend like you should not be leaving the Dragon Realm {name}...")
            time.sleep(1.5)
            print("Restarting the game in 3...")
            time.sleep(1)
            print("Restarting the game in 2...")
            time.sleep(1)
            print("Restarting the game in 1...")
            time.sleep(1)
            print(f"Welcome back to the Dragon Realm Legend {name}!")

            #Path 4: If the user entered his/her common name and entered yes it will print a message and restart the game
        else:
            print(f"Seems like you want to crush the Dragon Realm {name}!")
            time.sleep(1.5)
            print("It doesn't matter if you die or not, you will always be remembered as a true champion in the Dragon Realm!")
            time.sleep(1.5)
            print("Restarting the game in 3...")
            time.sleep(1)
            print("Restarting the game in 2...")
            time.sleep(1)
            print("Restarting the game in 1...")
            time.sleep(1)
            print(f"Welcome back to the Dragon Realm! Ultimate Champion {name}!")
            time.sleep(1.5)