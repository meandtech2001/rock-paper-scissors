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

choice=int(input("What do you choose? Type 0 for rock, 1 for Paper and 2 for Scissors."))

game=[rock,paper,scissors]
print(game[choice])

print("Computer chose:")

com=random.randint(0,2)
print(game[com])


if((choice==0 and com==1) or (choice==1 and com==2)or (choice==2 and com==0)):
 print("You lose")

elif((choice==1 and com==0) or (choice==2 and com==1) or (choice==0 and com==2)):
 print("You win")

elif(choice == com):
  print("Draw")
