import random

rpsls = ("rock", "paper", "scissors", "lizard", "spock")
rnd = 0
print()
print("""You are going to play rock, paper, scissors, lizard, spock since you thought that the normal rock, paper, scissors was way too boring.
Here's how this abomination of a 'game' works but first, please press 'enter' to make sure you are ready to continue""")
ent = input("> ")
if ent == "":
    print("""Alright, fine, here are the rules :
          
          Rock beats scissors and lizard, but loses to paper and spock.
          Paper beats rock and spock, but loses to scissors and lizard.
          Scissors beats paper and lizard, but loses to rock and spock.
          Lizard beats paper and spock, but loses to rock and scissors.
          And spock beats rock and scissors, but looses to paper and lizard.
          
          With all of that out of the way, you are now ready to start the game
          """)
    while ent == "":
        computer = random.choice(rpsls)
        rnd += 1
        print("Round", rnd)
        print()
        player = input("What would you like to choose? : ")
        print()
        print(player)
        print(computer)
        if player == computer:
            print("Draw")
        elif player == "Rock" or player == "rock":
            if computer == "scissors" or computer == "lizard":
                print("You won!")
            elif computer == "paper" or computer == "spock":
                print("You loose!")
        elif player == "paper" or player == "Paper":
            if computer == "rock" or computer == "spock":
                print("You won!")
            elif computer == "scissors" or computer == "lizard":
                print("you loose!")
        elif player == "scissors" or player == "Scissors":
            if computer == "paper" or computer == "lizard":
                print("You won")
            elif computer == "rock" or computer == "spock":
                print("You loose!")
        elif player == "Lizard" or player == "lizard":
            if computer == "paper" or computer == "spock":
               print("You won!")
            elif computer == "rock" or computer == "scissors":
                print("You loose!")
        elif player == "Spock" or player == "spock":
            if computer == "rock" or computer == "scissors":
                print("You won!")
            elif computer == "paper" or computer == "lizard":
                print("You loose!")
        else:
            print("Wut? That's not an option! You loose!")
        ent = input("""Would you like to go another round? Please press 'enter' if so.
Please type anything other than 'enter', than 'enter' if you don't want to play again.
>""")

else:
    print("ok")
