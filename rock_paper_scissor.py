import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("450x350")
root.resizable(False, False)

# Scores
user_score = 0
computer_score = 0

# Game logic
def play(user_choice):
    global user_score, computer_score

    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    # Update labels
    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer Choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")

# Reset score
def reset_score():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")
    user_label.config(text="Your Choice: ")
    computer_label.config(text="Computer Choice: ")
    result_label.config(text="Result: ")

# Labels
user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 12))
computer_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Score -> You: {user_score} | Computer: {computer_score}", font=("Arial", 12))
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=12, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=12, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=12, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Reset button
reset_button = tk.Button(root, text="Reset Score", width=15, command=reset_score)
reset_button.pack(pady=10)

# Run the app
root.mainloop()
