print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
def gameOverReason(counter):
    match counter:
        case 0:
            print("GG dude, you felt in a dark hairy hole")
            return
        case 1:
            print("A fish bite your ballz, game over!")
            return
        case 2:
            print("GG te comieron por rata")
            return
        case 3:
            print("GG game over! you got burned")
            return
        case 4:
            print("GG game over!")
            return
        case _:
            return

direction= input("So, which path do you choose? Right or Left /n tip: something nasty is a head ")

counter = 0
if direction.lower() == 'left':
    print("Good job, you just avoided the nasty hole")
    counter += 1
    direction= input("now that you made it here, do you want to swim to the other side or wait? /n tip: careful with these waters ").lower()
    if direction == 'wait':
        print("well well, one last test sucker, lets see what you got")
        counter += 1
        direction= input("Now that you are in the last path to the treasure, pick a color, Blue, Red or Yellow. ").lower()
        if direction == "blue":
            counter += 1
            gameOverReason(counter)
        elif direction == "red":
            counter += 2
            gameOverReason(counter)
        elif direction == "yellow":
            print("Well done champ, you made it! the treasure is yours")
        else:
            gameOverReason(counter)        
    else:
        gameOverReason(counter)
else:
    gameOverReason(counter)    
    
        
        
