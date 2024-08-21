import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        
        #  Configure window size and position to start maximized
        self.root.state('zoomed')  # This makes the window maximized
        
        self.user_score = 0
        self.computer_score = 0
        
        self.create_widgets()
        
        # Bind fullscreen toggle to F11 key and exit fullscreen to ESC key
        self.root.bind('<F11>', self.toggle_fullscreen)
        self.root.bind('<Escape>', self.exit_fullscreen)
    
    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Rock, Paper, Scissors", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)
        
        # User choices frame
        self.choices_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.choices_frame.pack(pady=20)
        
        # Load and resize images
        self.rock_img = self.load_and_resize_image("rock.png")
        self.paper_img = self.load_and_resize_image("paper.png")
        self.scissors_img = self.load_and_resize_image("scissors.png")
        
        # Rock button
        self.rock_button = tk.Button(self.choices_frame, image=self.rock_img, command=lambda: self.play('rock'), bg="#f0f0f0", borderwidth=0)
        self.rock_button.grid(row=0, column=0, padx=10)
        
        # Paper button
        self.paper_button = tk.Button(self.choices_frame, image=self.paper_img, command=lambda: self.play('paper'), bg="#f0f0f0", borderwidth=0)
        self.paper_button.grid(row=0, column=1, padx=10)
        
        # Scissors button
        self.scissors_button = tk.Button(self.choices_frame, image=self.scissors_img, command=lambda: self.play('scissors'), bg="#f0f0f0", borderwidth=0)
        self.scissors_button.grid(row=0, column=2, padx=10)
        
        # Score labels
        self.user_score_label = tk.Label(self.root, text=f"User Score: {self.user_score}", font=("Helvetica", 14), bg="#f0f0f0")
        self.user_score_label.pack(pady=5)
        
        self.computer_score_label = tk.Label(self.root, text=f"Computer Score: {self.computer_score}", font=("Helvetica", 14), bg="#f0f0f0")
        self.computer_score_label.pack(pady=5)
        
        # Result label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14, "italic"), bg="#f0f0f0")
        self.result_label.pack(pady=10)
    
    def load_and_resize_image(self, file_path, size=(100, 100)):
        """Load an image and resize it to the specified size."""
        image = Image.open(file_path)
        image = image.resize(size, Image.LANCZOS)  # Updated to Image.LANCZOS
        return ImageTk.PhotoImage(image)
    
    def get_computer_choice(self):
        """Randomly select between rock, paper, or scissors."""
        choices = ['rock', 'paper', 'scissors']
        return random.choice(choices)
    
    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner based on the user's choice and the computer's choice."""
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'
    
    def play(self, user_choice):
        """Play a round and update scores."""
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)
        
        result_message = f"User chose {user_choice}.\nComputer chose {computer_choice}.\n"
        
        if winner == 'tie':
            result_message += "It's a tie!"
        elif winner == 'user':
            result_message += "You win!"
            self.user_score += 1
        else:
            result_message += "You lose!"
            self.computer_score += 1
        
        # Update the result label and scores
        self.result_label.config(text=result_message)
        self.user_score_label.config(text=f"User Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

        # Ask if the user wants to play again
        self.ask_play_again()

    def ask_play_again(self):
        """Ask the user if they want to play another round."""
        play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
        if not play_again:
            self.result_label.config(text="Thank you for playing! Close the window to exit.")
            self.root.bind("<Button-1>", self.close_app)  # Bind mouse click to close the application

    def close_app(self, event=None):
        """Close the application."""
        self.root.quit()

    def toggle_fullscreen(self, event=None):
        """Toggle fullscreen mode."""
        self.root.attributes("-fullscreen", not self.root.attributes("-fullscreen"))

    def exit_fullscreen(self, event=None):
        """Exit fullscreen mode."""
        self.root.attributes("-fullscreen", False)

def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
