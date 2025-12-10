import random
import time
import os

user_score = 100
play_cost = 5
payout_triple = 50
payout_diagonal = 30

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the Text-Based Slot Machine!")
print(f"You start with {user_score} points. Each play costs {play_cost} points.")
print("Match 3 symbols horizontally or diagonally to win!")
print("-" * 40)

while user_score >= play_cost:
    input("Press Enter to play! (or Ctrl+C to quit)")
    clear()

    user_score -= play_cost
    print(f"Current score: {user_score}")

    slot_numbers = [0] * 9 
    for _ in range(10): 
        clear()
        print(f"Current score: {user_score}")
        print("Rolling...")
        for i in range(9):
            slot_numbers[i] = random.randint(0, 9)

        print(f"|{slot_numbers[0]}|{slot_numbers[1]}|{slot_numbers[2]}|")
        print(f"|{slot_numbers[3]}|{slot_numbers[4]}|{slot_numbers[5]}|")
        print(f"|{slot_numbers[6]}|{slot_numbers[7]}|{slot_numbers[8]}|")
        time.sleep(0.2) 

   
    winnings = 0

   
    if slot_numbers[0] == slot_numbers[1] == slot_numbers[2]:
        winnings += payout_triple
        print("WIN! Top row triple match!")
    if slot_numbers[3] == slot_numbers[4] == slot_numbers[5]:
        winnings += payout_triple
        print("WIN! Middle row triple match!")
    if slot_numbers[6] == slot_numbers[7] == slot_numbers[8]:
        winnings += payout_triple
        print("WIN! Bottom row triple match!")

   
    if slot_numbers[0] == slot_numbers[4] == slot_numbers[8]:
        winnings += payout_diagonal
        print("WIN! Diagonal (top-left to bottom-right) match!")
    if slot_numbers[6] == slot_numbers[4] == slot_numbers[2]:
        winnings += payout_diagonal
        print("WIN! Diagonal (bottom-left to top-right) match!")

    if winnings > 0:
        user_score += winnings
        print(f"You won {winnings} points! New score: {user_score}")
    else:
        print("No win this round.")

    print("-" * 40)

print("Game Over! You ran out of points.")
print(f"Final score: {user_score}")
