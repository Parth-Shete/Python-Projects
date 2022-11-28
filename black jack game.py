# These are the rules of the game:-
# 1) Ace is considered 11 or 1 according to the game. If the score is greater than 21 then use as ace as 1 point.
# 2) Jack, Queen, King are considered as of 10 points.
# 3) There will be two players, you and the computer.
# 4) Close to 21 wins the game.
# 5) If the points on the cards adds to greater than 21 then the player who got that looses that game.


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


import random


def deal_cards():
    """Returns a random card from the deck."""  # this is the docstring.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # remove is used to search for the first instance of the given element and removes it.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over, you lose"
    elif computer_score > 21:
        return "Opponent went over, you win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


"""Take a list of cards and return the score calculated from the cards."""


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False  # Acts as a flag.

    for _ in range(2):
        user_cards.append(deal_cards())  # append is used to add a single element to the end of the list.
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your card's: {user_cards}, current score: {user_score}")
        print(
            f"Computer's first card: {computer_cards[0]}")  # '0' is used required so that the first card can be seen of
        # the computer.

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True  # This is to end the game.
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 or computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final_score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play the game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
