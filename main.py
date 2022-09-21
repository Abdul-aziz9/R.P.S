item = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']


import random

print('LETS PLAY ROCK, PAPER, SCISSORS')
end_of_game = False
user_score = 0
com_score = 0


while not end_of_game:
    user = int(input('pick either 0 for Rock, 1 for Paper or 2 for scissors '))
    try:
        com_val = item[random.randint(0,len(item)-1)]
        user_val = item[user]
        print(f'You chose:\n{user_val}\n Computer chose:{com_val}')
        if user_val == item[2] and com_val == item[0] :
            com_score += 1
            print(f'You lose\n User :{user_score}  computer :{com_score}')
        elif user_val == item[0] and com_val == item[2] :
            user_score += 1
            print(f'You Win\n User :{user_score}  computer :{com_score}')
        elif user_val == item[1] and com_val == item[0] :
            user_score += 1
            print(f'You Win\n User :{user_score}  computer :{com_score}')
        elif user_val == item[0] and com_val == item[1] :
            com_score += 1
            print(f'You lose\n User :{user_score}  computer :{com_score}')
        elif user_val == item[1] and com_val == item[2] :
            com_score += 1
            print(f'You lose\n User :{user_score}  computer :{com_score}')
        elif user_val == item[2] and com_val == item[1] :
            user_score += 1
            print(f'You Win\n User :{user_score}  computer :{com_score}')
        else:
            print(f"it's a tie\n User :{user_score}  computer :{com_score}")
        
        if user_score == 10 or com_score == 10 :
            print(f'Final score \n User :{user_score}  computer :{com_score}')
            if com_score > user_score:
                print('You Lose')
            else:
                print('You Win!')
            break
    except:
        user > 2 or user < 0
        print('you entered an invalid number')
