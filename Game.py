def game():
    number = 15
    chance = 1
    print('\n-----Welcome to the game "Guess the number-----')
    print("You have 5 chances to finish th game")
    while(chance <=5 ):
        print('\nEnter the number:')
        user = int(input())
        if user < number:
            print(f"Try Again! - Your number is smaller     (Chances left: {5 - chance})")
        elif user > number:
            print(f"Try Again! - Your number is Bigger     (Chances left: {5 - chance})")
        else:
            print(f"You won! You took {chance} chances to complete the game")
            break
        chance +=1

        if chance > 5:
            print("You are out of chances! Game over!")
            print('The number was 15')
game()
replay = input("Do you want to play again[yes/no]:")
if replay == 'yes':
    game()
else:
    print('Thanks for playing')