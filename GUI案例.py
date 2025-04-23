"""
#案例1
import tkinter as tk

root = tk.Tk()
root.title('英尺/米转换器')

def func():

    value = entry.get()

    res = (0.3048 * float(value) * 10000 + 0.5) / 10000

    root_label["text"] = f"{round(res,2)}"


frm = tk.Frame(root,relief = tk.SUNKEN,borderwidth = 3)

entry = tk.Entry(frm,width = 10)
label = tk.Label(frm,text = '英尺')

entry.grid(row = 0,column = 0)
label.grid(row = 0,column =1)

btn = tk.Button(root,text = "\N{RIGHTWARDS BLACK ARROW}",command = func)
root_label = tk.Label(root,text = '米')

frm.grid(row = 0,column = 0,padx = 10)
btn. grid(row = 0,column = 1,pady = 10)
root_label.grid(row = 0,column = 2,padx = 10)

root.mainloop()


#案例2
import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")

window.resizable(width = False,height = False)   #控制窗口是否可以被用户调整大小,接受两个布尔值参数

def func():

    value = ent_temp.get()

    res = (5 / 9) * (float(value) - 32)

    lbl_result["text"] = f"{round(res, 2)} \N{DEGREE CELSIUS}"


frm_entry = tk.Frame(window)
ent_temp = tk.Entry(frm_entry,width = 10)
lbl_temp = tk.Label(frm_entry,text = "华氏度")

ent_temp.grid(row = 0,column = 0)
lbl_temp.grid(row = 0,column = 1)

btn_con = tk.Button(window,text = "\N{RIGHTWARDS BLACK ARROW}",command = func)
lbl_result = tk.Label(window, text="摄氏度")

frm_entry.grid(row = 0,column = 0,padx = 10)
btn_con.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()


#案例3(文本编辑器)

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = tk.Tk()
root.title("Simple Text Editor")


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    root.title(f"Simple Text Editor - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    root.title(f"Simple Text Editor - {filepath}")


root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(root)
frm = tk.Frame(root,relief = tk.RAISED, bd=5)
btn_1 = tk.Button(frm,text = 'open',command = open_file)
btn_2 = tk.Button(frm,text = 'Save As...',command = save_file)

btn_1.grid(row = 0,column = 0, sticky="ew", padx=5, pady=5)
btn_2.grid(row = 0,column = 1, sticky="ew", padx=5)

txt_edit.grid(row = 0,column = 1,sticky = 'nsew')
frm.grid(row = 0,column = 0, sticky="ns")

root.mainloop()


#案例4(井字棋)
import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple

class Player(NamedTuple):
    label: str
    color: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)

class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

    def toggle_player(self):
        self.current_player = next(self._players)

    def is_valid_move(self, move):
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played

    def process_move(self, move):
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(self._current_moves[n][m].label for n, m in combo)
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        return self._has_winner

    def is_tied(self):
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)

    def reset_game(self):
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
        self._has_winner = False
        self.winner_combo = []

class TicTacToeBoard(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}
        self._game = game
        self._create_menu()
        self._create_board_display()
        self._create_board_grid()

    def _create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="Play Again", command=self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def play(self, event):
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)
            if self._game.is_tied():
                self._update_display(msg="Tied game!", color="red")
            elif self._game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    def reset_board(self):
        self._game.reset_game()
        self._update_display(msg="Ready?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")

def main():
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()

if __name__ == "__main__":
    main()



#案例5

import tkinter as tk

root = tk.Tk()
root.geometry("130x250")
root.title("Calculator")

def ev_al():
    res = eval(entry.get())
    entry.delete(0,tk.END)
    entry.insert(tk.END,str(res))

def clear():
    entry.delete(0,tk.END)

def clear_1():
    entry.delete(len(entry.get()) - 1,tk.END)

frm = tk.Frame(root)
frm.grid(row=2,column=0,sticky='nsew')

entry = tk.Entry(root,width=19)
entry.grid(row=0,column=0,sticky='ew',padx=5,pady=5)

buttoms = [
    '7','8','9','*',
    '4','5','6','-',
    '1','2','3','+',
    '.','0','=','/',
    '(',')','C','DE'
]

row_num = 1
col_num = 0

for buttom in buttoms:
    command = lambda x = buttom:entry.insert(tk.END,x) if x != '=' else ev_al()
    if buttom == 'C':
        tk.Button(frm,text=buttom,command=clear).grid(row=row_num,column=col_num,padx=2,pady=2,ipadx=5,ipady=5,sticky='nsew')
    elif buttom == 'DE':
        tk.Button(frm,text=buttom,command=clear_1).grid(row=row_num,column=col_num,padx=2,pady=2,ipadx=5,ipady=5,sticky='nsew')
    else:
        tk.Button(frm,text=buttom,command=command).grid(row=row_num,column=col_num,padx=2,pady=2,ipadx=5,ipady=5,sticky='nsew')
    col_num += 1
    if col_num == 4:
        col_num = 0
        row_num += 1

root.mainloop()
"""