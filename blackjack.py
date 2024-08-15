import random
# import clear
from blackjack_art import logo

def deal_card():
    '''Draws and returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    '''Evaluates the score of the given hand'''
    # Check for blackjack (a hand with only 2 cards: ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Adjust for ace if the score exceeds 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    '''Compares the final scores and returns the result'''
    if user_score > 21 and computer_score > 21:
        return "Both scores are over 21. You lose 😒"
    
    if user_score == computer_score:
        return "It's a tie 🤔"
    elif computer_score == 0:
        return "Opponent has Blackjack. You lose 😱"
    elif user_score == 0:
        return "You hit Blackjack! You win 😎"
    elif user_score > 21:
        return "Your score exceeded 21. You lose 😒"
    elif computer_score > 21:
        return "Opponent exceeded 21. You win 😁"
    elif user_score > computer_score:
        return "Congratulations, you win! 🙌"
    else:
        return "Sorry, you lose 😤"

def play_game():
    
    print(logo)
    
    # Initialize hands and game state
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    # Initial dealing of cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:
        # Recalculate scores with each new card
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your hand: {user_cards}, current score: {user_score} ")
        print(f"   Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True 
        else:
            # Offer the user a choice to draw another card or pass
            user_should_deal = input("Type 'y' to draw another card, type 'n' to hold: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True 
    
    # Computer's turn to draw cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
# Prompt user to play again
while input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # clear
    play_game()
