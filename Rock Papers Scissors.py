import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x500")

# Variables to store scores
player_score = 0
computer_score = 0

# Function to update the score
def update_score(result):
    global player_score, computer_score
    if result == "Player":
        player_score += 1
    elif result == "Computer":
        computer_score += 1
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")

# Function to reset the game
def reset_game():
    result_label.config(text="")
    player_choice_label.config(text="Player: ")
    computer_choice_label.config(text="Computer: ")
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")

# Function to disable buttons
def disable_buttons():
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")

# Function to enable buttons
def enable_buttons():
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")

# Function to play the game
def play(choice):
    global player_score, computer_score
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    player_choice_label.config(text=f"Player: {choice}")
    computer_choice_label.config(text=f"Computer: {computer_choice}")

    if choice == computer_choice:
        result = "Draw"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "Player"
    else:
        result = "Computer"

    result_label.config(text=f"Result: {result}")
    update_score(result)
    disable_buttons()

# GUI Elements
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20))
title_label.pack(pady=10)

player_choice_label = tk.Label(root, text="Player: ", font=("Arial", 15))
player_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer: ", font=("Arial", 15))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 15))
result_label.pack(pady=5)

score_label = tk.Label(root, text="Player: 0  Computer: 0", font=("Arial", 15))
score_label.pack(pady=5)

rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

# Reset button
reset_button = tk.Button(root, text="RESET", width=10, command=reset_game)
reset_button.pack(pady=20)

# Run the main loop
root.mainloop()