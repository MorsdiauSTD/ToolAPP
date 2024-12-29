import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        self.instruction_label = tk.Label(self.root, text="Guess a number between 1 and 100:")
        self.instruction_label.pack()
        
        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()
        
        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        
    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            
            if guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
    
    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()