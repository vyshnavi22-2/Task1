import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.buttons = []
        self.create_ui()

    def create_ui(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=('Helvetica', 24), height=2, width=5,
                            command=lambda i=i: self.handle_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

        reset_btn = tk.Button(self.root, text="Reset", font=('Helvetica', 14), command=self.reset_game)
        reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def handle_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def reset_game(self):
        self.board = ["" for _ in range(9)]
        for btn in self.buttons:
            btn.config(text="")
        self.current_player = "X"

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()