from random import randint
def win():
    print("you win!")
def lose():
    print("you lose!")    
while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]
    print(computer_choice,"computer choice")
    if player_choice == computer_choice:
        print ('Draw!')
    elif  player_choice == 'rock' and computer_choice == 'scissors':
        win()
    elif  player_choice == 'paper' and computer_choice == 'scissors':
        lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
        win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
        lose()
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
    elif player_choice =='rock'  and computer_choice =='paper' :
        lose()
    else:
        again = input('Do you want to play again yes or no  ')
        if again == 'yes':
            print("yes")
            continue
        else:
            print("no")
            break


