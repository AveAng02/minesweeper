from asyncio.windows_events import NULL
from tkinter import Button, Label
import random
from turtle import width
import settings
import ctypes
# import math

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    player_score = 0
    cell_mine_count = []
    cell_count_lable_object = None
    score_card = None

    def __init__(self, x, y, is_mine = False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.is_mine_candidate = False
        self.is_opened = False
        self.cell_btn_onj = None

        # Append the object to the list
        Cell.all.append(self)

    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=9,
            height=3
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_onj = btn

    @staticmethod
    def create_cell_count_table(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left : {Cell.cell_count}",
            width=12,
            height=4,
            font=("", 30)
        )
        Cell.cell_count_lable_object = lbl

    
    @staticmethod
    def create_score_card(location):
        sc = Label(
            location,
            bg='black',
            fg='white',
            text=f"Score : {Cell.player_score}",
            width=12,
            height=4,
            font=("", 30)
        )
        Cell.score_card = sc

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]

        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            Cell.player_score += 1
            self.cell_btn_onj.configure(bg = 'SystemButtonFace',text=self.surrounded_cells_mines_length)
            # Replace the text of cell count label with the newer count
            if Cell.cell_count_lable_object:
                Cell.cell_count_lable_object.configure(text=f"Cells Left : {Cell.cell_count}")
                Cell.score_card.configure(text=f"Score : {Cell.player_score}")

        # Mark the cell as opened
        self.is_opened = True


    def show_mine(self):
        # a logic to interrupt the game and 
        # display that the player have lost
        # and an option to restart
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 1)
        self.cell_btn_onj.configure(bg='red', text='mine')


    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_onj.configure(
                bg = 'orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_onj.configure(
                bg = 'SystemButtonFace'
            )
            self.is_mine_candidate = False


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINE_COUNT
        )

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self) -> str:
        return f"Cell({self.x}, {self.y})"



    


