import random
import time

#randomly generate 4 digit code
def generate_code():
    return [random.randint(0, 9) for _ in range(4)]

#checks is the guess againt the code and returns the number of correct digit
def check_guess(code, guess):
    correct_positions = sum(1 for i in range(4) if code[i] == guess[i])
    if correct_positions == 4:
        return True, correct_positions
    elif correct_positions > 0:
        return False, correct_positions
    else:
        return False, 0
1as

print("Welcome to the Code Breaker game!")
print("Try to guess the 4-digit code.")

code = generate_code()
# starts the timer
start_time = time.time()
#counts the number of attempts
attempts = 0
while True:
    #Gets the player guess
    guess = input("Enter your guess (4 digits): ")
    #checks if the guess if valid
    if len(guess) != 4 or not guess.isdigit():
        print("Please enter a 4-digit number.")
        continue

    guess = [int(digit) for digit in guess]
    attempts += 1

    correct, correct_positions = check_guess(code, guess)
    if correct:
        #Ends the timer 
        end_time = time.time()
        elapsed_time = end_time - start_time
        #Prints success message, number of attempts and time
        print(f"Congratulations! You guessed the code in {attempts} attempts and {elapsed_time:.2f} seconds.")
        break
    else:
        #feedback on correct positions
        print(f"Correct positions: {correct_positions}")

