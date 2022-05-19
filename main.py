from tkinter import *
from cell import Cell
import settings
import utils

# Window settings
root = Tk()
root.configure(bg='grey')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper')
root.resizable(False, False)

# Frame Definitions
top_frame = Frame(
    root,
    bg = 'orange',
    width = settings.WIDTH,
    height = utils.percentage(settings.HEIGHT, 25)
)

left_frame = Frame(
    root,
    bg = 'cyan',
    width = utils.percentage(settings.WIDTH, 25),
    height = utils.percentage(settings.HEIGHT, 75)
)

center_frame = Frame(
    root,
    bg = 'white',
    width = utils.percentage(settings.WIDTH, 75),
    height = utils.percentage(settings.HEIGHT, 75)
)
#########################################

# Frame initializations
top_frame.place(x = 0, y = 0)
left_frame.place(x = 0, y = 180)
center_frame.place(x = utils.percentage(settings.WIDTH, 25), y = utils.percentage(settings.HEIGHT, 25))

# Button generation
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c1 = Cell(x, y)
        c1.create_btn_obj(center_frame)
        c1.cell_btn_onj.grid(
            column=x,
            row=y
        )
#######################################

# Call the label from cell class 
Cell.create_cell_count_table(left_frame)

Cell.cell_count_lable_object.place(
    x = 0,
    y = 0
)

Cell.randomize_mines()
#Cell.algorithm()

# Window run
root.mainloop()
