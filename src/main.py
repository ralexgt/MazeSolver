from graphics import *
from maze import Maze
import time

def main():
  # maze size
  num_rows = 40
  num_cols = 46
  
  # window size
  margin = 50
  screen_x = 1200
  screen_y = 1000
  
  # individual cell size
  cell_size_x = (screen_x - 2 * margin) / num_cols
  cell_size_y = (screen_y - 2 * margin) / num_rows
  win = Window(screen_x, screen_y)

  # take seed from current time to fake randomness
  time_now = round(time.time() * 1000)
  print(f"Maze built with seed: {time_now}")
  maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=time_now)
  
  win.wait_for_close()

main()