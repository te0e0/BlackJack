import platform
import os
#to clear screen
def clr_scr():
    # Check if the platform is Windows or linux
    # If Platform is Windows then run command os.system(‘cls’) else os.system(‘clear’)
    if (platform.system().lower() == "windows"):
        cmdtorun = 'cls'
    else:
        cmdtorun = 'clear'

    os.system(cmdtorun)


from Dealing import Player
from art import logo

user = Player()
dealer = Player()

def initial_deal_and_score():
    user.deal_cards(2)
    dealer.deal_cards(2)
    user.score_hand()
    dealer.score_hand()
def deal_and_score(player):
    ''''player = who to deal card to'''
    player.deal_cards(1)
    user.score_hand()
    dealer.score_hand()
def hitting_cards():
    more_cards = input("Do you wish to hit? (y / n)").lower()
    if more_cards == "y":
        deal_and_score(user)
        if user.score > 21:
            print(f"Your cards are {user.display_cards(2)}. You Busted!")
            play_again = input("Press ENTER to play again")
            clr_scr()
            game()
        else:
            print(f"Your cards are {user.display_cards(2)}")
            hitting_cards()
def reset():
    user.reset()
    dealer.reset()


#putting the entire game into a function to allow for recursion
def game():
    reset()
    print(logo)
    ##leaving room for betting procedure

    initial_deal_and_score()

    if dealer.score == 21:
        Play_again = input(f"Your cards are {user.display_cards(2)}. The dealer is showing the following cards: "
                           f"[{dealer.display_cards(2)}. Sorry,the dealer got BlackJack! Press Enter to play again")
        user.reset()
        game()

    if user.score == 21:
        Play_again = input(f"Your cards are {user.display_cards(2)}. The dealer is showing the following cards: "
                           f"{dealer.display_cards(2)}. Congratulations, you got BlackJack! Press Enter to play again")
        user.reset()
        game()

    print(f"Your cards are {user.display_cards(2)}. The dealer is showing the following cards: "
          f"{dealer.display_cards(1)}")





    hitting_cards()
game()







