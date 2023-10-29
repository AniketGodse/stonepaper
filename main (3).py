import random

def play_game(user, comp):
    if user == comp:
        return -1
    if user == 's' and comp == 'p':
        return 0
    elif user == 'p' and comp == 's':
        return 1
    if user == 's' and comp == 'z':
        return 1
    elif user == 'z' and comp == 's':
        return 0
    if user == 'p' and comp == 'z':
        return 0
    elif user == 'z' and comp == 'p':
        return 1

if __name__ == "__main__":
    user_choice = ''
    comp_choice = ''
    result = ''

    random.seed()
    n = random.randint(0, 99)

    if n < 33:
        comp_choice = 's'
    elif 33 <= n < 66:
        comp_choice = 'p'
    else:
        comp_choice = 'z'

    print("Your move: (s)tone, (p)aper, (z)scissors")
    user_choice = input().lower()

    result = play_game(user_choice, comp_choice)

    if result == -1:
        print("It's a draw!")
    elif result == 0:
        print(f"You lose! Computer chose {comp_choice}.")
    elif result == 1:
        print(f"You win! Computer chose {comp_choice}.")
