import random
dealerBust = False
playerBust = False
playerHold = False
dealerHold = False
dGame = False
King = Queen = Jack = 10
Ace = 1
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace]
dealerScore = 0
playerScore = 0


def deal_card():
    global playerScore
    global playerHold
    if not playerHold:
        deal = str(input("do you want to get a card? [y/n]: "))
        if deal == 'y':
            c = cards[random.randint(0, 12)]
            print(name, 'got a', c)
            playerScore += c
            print(playerScore)
        elif deal == 'n':
            playerHold = True


def dealerDraw():
    global dealerHold
    global dealerScore
    if not dealerHold:
        if dealerScore <= 21:
            w = cards[random.randint(0, 12)]
            dealerScore += w
        else:
            dealerHold = True


def isBust(score):
    if score > 21:
        return True


def checkWin(dealerScore, playerScore):
    global endGame
    if isBust(playerScore) and isBust(dealerScore):
        print("Player: ", playerScore, "Dealer: ", dealerScore)
        print("both of you lost, lol")
        endGame = True
    elif playerScore == 21 or not isBust(playerScore) and isBust(dealerScore) or playerScore > dealerScore and playerHold:
        print("Player: ", playerScore, "Dealer: ", dealerScore)
        print(name, 'wins! Good Job!')
        endGame = True
    elif dealerScore == 21 or isBust(playerScore) and not isBust(dealerScore) or playerScore < dealerScore and dealerHold:
        print("Player: ", playerScore, "Dealer: ", dealerScore)
        print("Dealers win! Rough Luck :(")
        endGame = True


print("Lets play some Black jack!!")
name = str(input("what is your name?: "))
print('Hello', name, 'lets do this thing!')

while not endGame:
    deal_card()
    dealerDraw()
    isBust(playerScore)
    isBust(dealerScore)
    checkWin(dealerScore, playerScore)