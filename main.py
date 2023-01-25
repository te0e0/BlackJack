import os
from Dealing import Player
from art import logo

user = Player()
dealer = Player()

#putting the entire game into a function to allow for recursion
def game():
    print(logo)
    ##leaving room for betting procedure

    user.deal_cards(2)
    dealer.deal_cards(2)
    user.score_hand()
    dealer.score_hand()

    if dealer.score == 21:
        Play_again = input("Sorry,the dealer got BlackJack! Press Enter to play again")
        user.reset()
        game()

    if user.score == 21:
        Play_again = input("BlackJack! Press Enter to play again")
        user.reset()
        game()

    print(f"Your cards are {user.display_cards(2)}. The dealer is showing an [{dealer.display_cards(1)}]")
    more_cards = input("Do you wish to hit? (y / n)").lower()

    if more_cards == "y":
        user.deal_cards(1)
        user.score_hand()
        user.reset()
        dealer.reset()
        game()

        if user.score > 21:
            print("you busted!")
            game()

        else:
            print(f"Your cards are {user.display_cards(2)}")


game()







