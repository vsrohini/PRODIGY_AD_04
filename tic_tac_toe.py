import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.board = [None] * 9  # Represent the 3x3 board
        self.current_player = "X"  # X starts the game
        self.buttons = []
        
        # Create the Tic-Tac-Toe buttons
        for i in range(9):
            button = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
        
        # Create the Reset button
        self.reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), width=20, command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)
        
    def make_move(self, index):
        # If the spot is empty, make a move
        if self.board[index] is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif all(cell is not None for cell in self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                
    def check_winner(self, player):
        # Check all possible win combinations
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]               # diagonals
        ]
        for combo in win_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False
        
    def disable_buttons(self):
        # Disable all the buttons after the game is over
        for button in self.buttons:
            button.config(state="disabled")
        
    def reset_game(self):
        # Reset the game state
        self.board = [None] * 9
        self.current_player = "X"
        for i in range(9):
            self.buttons[i].config(text="", state="normal")
        
# Create the main window
root = tk.Tk()

# Create the TicTacToe game
game = TicTacToe(root)

# Start the GUI event loop
root.mainloop()
