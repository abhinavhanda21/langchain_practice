import random

Computer_choice = random.choice(['Rock', 'Paper', 'Scissor']) 
user_choice =input('Rock, Paper or Scissor?')

if Computer_choice == user_choice:
   print("TIE")
elif Computer_choice == 'Paper' and user_choice == 'Scissor':
   print ("User Wins")
elif Computer_choice == 'Rock' and user_choice == 'Paper':
   print ("Computer wins")
elif Computer_choice == 'Scissor' and user_choice == 'Paper':
   print ("Computer wins")
