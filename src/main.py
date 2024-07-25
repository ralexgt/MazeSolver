from graphics import *
from maze import *
import time

def main():
  # maze size
  num_rows = 18
  num_cols = 20
  
  # window size
  margin = 50
  screen_x = 800
  screen_y = 600
  
  # individual cell size
  cell_size_x = (screen_x - 2 * margin) / num_cols
  cell_size_y = (screen_y - 2 * margin) / num_rows
  win = Window(screen_x, screen_y)

  # take seed from current time to fake randomness
  time_at_creation = round(time.time())
  print(f"Maze built with seed: {time_at_creation}")
  print(f"Maze with {num_rows} rows and {num_cols} colons")
  maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=time_at_creation)
  print(f"Maze created in {round(time.time()) - time_at_creation} seconds, having a {animation_delay_create} seconds animation delay")
  
  # try solving the maze | is_solvea
  time_at_solving = round(time.time())
  is_solvable = maze.solve()
  if not is_solvable:
    print("No correct path for this maze!")
  else:
    print("Maze was solved!")
  print(f"Maze solved in {round(time.time()) - time_at_solving} seconds, having a {animation_delay_solve} seconds animation delay")
  win.wait_for_close()

main()