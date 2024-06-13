import random
import time


def generate_random_number(digits):      # Generates a random number with given number of digits.
    return random.randint(10**( digits-1), (10** digits)-1)

def get_user_guess(digits):              # Prompts the user to guess the secret number
    return int(input(f"\nGuess the number between {10**( digits-1)}-{(10** digits)-1}: "))

def set_difficulty(digits,difficulty):   # Returns the number of attempts a player can use
    if difficulty=='1' or difficulty=='easy':
         return 10**digits
    if difficulty=='2' or difficulty=='medium':
         return 8**digits
    if difficulty=='3' or difficulty=='hard':
         return 5**digits

def compare_guess(digits,secret_num, user_guess):    # Compare the digits in user's guess and the secret number
    count = 0
    correct_digits = ['X'] *  digits
    for i in range( digits):
        if str(secret_num)[i] == str(user_guess)[i]:
            count += 1
            correct_digits[i] = str(secret_num)[i]
    return count, correct_digits

def evaluate_guess(digits,secret_num,user_guess):   # Checks whether the user's guess matches the secret number
    if user_guess == secret_num:
            return 1
    count, correct_digits =  compare_guess(digits,secret_num, user_guess)
    if count == 0:
            print("\nNo number in your input match.\n")
            return 0
    else:
            print("\nNot quite the number. But you did get", count, "digit(s) correct!\n")
    print("Also these numbers in your input were correct:", " ".join(correct_digits))
    print("\n")
    return

def main():
    players = int(input("\n1 player\n2 players\n3 players\n4 players\nEnter no.of Players: "))
    scores = []
    digits = int(input("\nEnter number of digits in the number you want to guess: "))
    difficulty = input('\n1. Easy\n2. Medium\n3. Hard\nSelect the difficulty: ')
    total_tries = set_difficulty(digits,difficulty)
    curr_player = 1
    while curr_player <= players:

        print(f"Player {curr_player}'s turn to play:\n")
        timer =['1️⃣','2️⃣','3️⃣']
        for i in timer[::-1]:
             print('\t',i)
             time.sleep(1)
        secret_num =generate_random_number(digits)

        attempts = 0

        while True:
            if attempts>total_tries:
                 print('\nYour attempts exceeded. BETTER LUCK NEXT TIME.😊\n')
                 break
            user_guess = get_user_guess(digits)
            attempts += 1

            if evaluate_guess(digits,secret_num,user_guess):
                 print("\nCongratulations! You guessed the number in", attempts, "attempts.\n\n")
                 time.sleep(2)
                 break
            else:
                 continue
        scores.append((curr_player,attempts))
        curr_player += 1

    if players > 1:
        scores.sort()
        print("\nThe MASTERMIND is:\n")
        print("\n\t🎊🎉🎉 Player",scores[0][0],"🎉🎉🎊\n\n")

if __name__ == "__main__":
    main()
