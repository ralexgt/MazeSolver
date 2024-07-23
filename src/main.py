from graphics import *

def main():
  win = Window(800, 600)
  fill_color = "red" # line color
  p1, p2, p3, p4, p5, p6 = Point(10, 122), Point(155, 322), Point(200, 400), Point(300, 300), Point(50, 200), Point(75, 599)
  lines = [Line(p1, p2), Line(p3, p4),]# Line(p2, p5), Line(p4, p6), Line(p4, p5), Line(p6, p6)]
  for line in lines:
    win.draw_line(line, fill_color)
  
  win.wait_for_close()

main()