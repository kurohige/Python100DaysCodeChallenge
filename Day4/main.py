import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
aiSelect = int(random.randrange(3))
userSelect = int(input("This is the end of the line mofo,\nis your time to choose \nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))


if userSelect == 0:
  print(rock)
  if aiSelect == 1:
    print(paper)
    print("GG bitch, you lose!")
  elif aiSelect == 2:
    print(scissors)
    print("Not bad, not bad, you win!")
  else:
    print(rock)
    print("Well, Well, it seems we have a draw")
elif userSelect == 1:
  print(paper)
  if aiSelect == 2:
    print("GG bitch, you lose!")
  elif aiSelect == 0:
    print(rock)
    print("Not bad, not bad, you win!")
  else:
    print(paper)
    print("Well, Well, it seems we have a draw")
elif userSelect == 2:
  print(scissors)
  if aiSelect == 0:
    print(rock)
    print("GG bitch, you lose!")
  elif aiSelect == 1:
    print(paper)
    print("Not bad, not bad, you win!")
  else:
    print(scissors)
    print("Well, Well, it seems we have a draw")
else:
  print("try again")
