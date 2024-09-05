import tkinter as tk
from tkinter import messagebox
import numpy as np

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = np.array([[" " for _ in range(3)] for _ in range(3)])
        self.current_player = "X"  # Human player is always "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text=" ", font=("Arial", 24),
                                                width=5, height=2,
                                                command=lambda i=i, j=j: self.player_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def player_move(self, i, j):
        if self.board[i][j] == " ":
            self.board[i][j] = self.current_player  # Mark the board with "X"
            self.buttons[i][j].config(text=self.current_player)
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O"  # Switch to computer player
                self.computer_move()

    def computer_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        self.board[best_move[0]][best_move[1]] = "O"
        self.buttons[best_move[0]][best_move[1]].config(text="O")
        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.reset_game()
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
        else:
            self.current_player = "X"  # Switch back to human player

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner_minimax(board)
        if winner == "O":
            return 1  # AI wins
        elif winner == "X":
            return -1  # Player wins
        elif self.is_draw():
            return 0  # Draw

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = " "
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = " "
                        best_score = min(best_score, score)
            return best_score

    def check_winner_minimax(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != " ":
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]
        return None

    def check_winner(self):
        return self.check_winner_minimax(self.board)

    def is_draw(self):
        return " " not in self.board

    def reset_game(self):
        self.board = np.array([[" " for _ in range(3)] for _ in range(3)])
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
        self.current_player = "X"  # Reset to human player "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()