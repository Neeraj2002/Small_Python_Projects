import random

def main():
    player1 = 0
    player1wins = 0
    player2wins = 0
    player2 = 0
    rounds = 1
    Player1 = input("Enter your name: ")
    Player2 = input("Enter your name: ")



    for rounds in range(1,7,1):
        print(f"Round {str(rounds)} ", end="")
        player1 = dice_roll()
        player2 = dice_roll()
        print(f"| {Player1}: {player1} ", end="")
        print(f"| {Player2}: {player2}")

        if player1 == player2:
            print("Draw!")
        elif player1 > player2:
            print(f"{Player1} wins!")
            player1wins += 1
        else:
            print(f"{Player2} wins!")
            player2wins += 1


        rounds += 1

    if player1wins == player2wins:
        print(f"{Player1} Rounds won by {player1wins}\n"
              f"{Player2} Rounds won by {player2wins}\n"
              f"Draw!")

    elif player1 > player2:
        print(f"{Player1} Rounds won by {player1wins}\n"
              f"{Player2} Rounds won by {player2wins}\n"
              f"{Player1} wins!\n")
    else:
        print(f"{Player1} Rounds won by {player1wins}\n"
              f"{Player2} Rounds won by {player2wins}\n"
              f"{Player2} wins!\n")


def dice_roll():
    diceroll = random.randint(1, 6)
    return diceroll

main()

