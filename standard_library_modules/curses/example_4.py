# w a s d 

import curses
import time


screen = curses.initscr()
curses.noecho()
dimensions = screen.getmaxyx()
screen.nodelay(1)
q = -1
x, y = 0, 0
while q != ord("q"):
    screen.clear()
    screen.addstr(y, x, "<<< CEVHERİ !", curses.A_BOLD)
    screen.refresh()
    q = screen.getch()
    if q == ord("w") and y > 0:
        y -= 1
    elif q == ord("s") and y < dimensions[0] - 1:
        y += 1
    elif q == ord("a") and x > 0:
        x -= 1
    elif q == ord("d") and x < dimensions[1] - len("<<< CEVHERİ !") - 1:
        x += 1
    time.sleep(0.05)
curses.endwin()
