import random
rps = ['rock', 'paper', 'scissor']

def playrps():
    x = random.choice(rps)
    cpumove = rps.index(x)
    # chooses a random element from rps and returns the position value of that element
    # and assigns to the variable cpumove
    print('CPU: Lets play!')
    # print(x) prints the CPU's move for testing purposes only
    userinput = input("What's your move? rock, paper, or scissors?: ")
    while True:
        if userinput == 'rock':
            usermove = 2
            break
        elif userinput == 'paper':
            usermove = 1
            break
        elif userinput == 'scissor':
            usermove = 0
            break
        else:
            print('Invalid input. Please try again.')
            continue
    if usermove + cpumove == 4 or usermove + cpumove == 1:
        print('Congrats! You win!')
    elif usermove + cpumove == 3 or usermove + cpumove == 0:
        print('You Lose and you SUCK!')
    elif usermove + cpumove == 2:
        print("It's a TIE! Rematch!")
        playrps()
    playagain()

def playagain():
    askreplay = input('Wanna play again? Type "y" for yes or "n" for no: ')
    if askreplay == 'y':
        playrps()
    elif askreplay == 'n':
        print('Thanks for playing!')
        quit()

askplayagame = input('CPU: Wanna play rock paper scissors? Type "y" for yes or "n" for no: ')
if askplayagame == 'y':
    playrps()
elif askplayagame == 'n':
    print('COWARD!')
    quit()










