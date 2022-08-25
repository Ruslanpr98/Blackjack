import random
from replit import clear

def deal_card(cards):
  return random.choice(cards)


def calculate_score(card):
  if sum(card) == 21 and len(card) == 2:
    return 0
  elif 11 in card:
    if sum(card) > 21:
      card.remove(11)
      card.append(1)
  return sum(card)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Computer wins"
  elif user_score > 21:
    return "User lost. Computer wins"
  elif computer_score > 21:
    return "Computer lost. User wins"
  elif computer_score > user_score:
    return "User lost. Computer wins"
  else:
    return "Computer lost. User wins"


def game():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
  user_cards = []
  computer_cards = []
  game_over = False
  
  user_cards.append(deal_card(cards))
  user_cards.append(deal_card(cards))
  
  computer_cards.append(deal_card(cards))
  computer_cards.append(deal_card(cards))
  
  
  print(user_cards)
  
  print(computer_cards)
  
  while not game_over:
    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    
    
    if computer_score == 0 or user_score == 0 or user_score > 21:
      game_over = True
    else:
      decision = input("Do the user want to draw another card?\n")
      if decision == 'yes':
        user_cards.append(deal_card(cards))
        print(f"User cards {user_cards}")
        print(f"Computer cards {computer_cards}")
      else:
        game_over = True
        #print("The game ended")
  
  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card(cards))
    computer_score = calculate_score(computer_cards)
  
  print("----------------------------------------------")
  print(f"User final cards {user_cards}")
  print(f"Computer final cards {computer_cards}")
  print(compare(user_score,computer_score))

while input("Do you want to play the game?\n") == 'yes':
  clear()
  game()
