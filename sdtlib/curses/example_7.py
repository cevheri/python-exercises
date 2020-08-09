#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time

ekran = curses.initscr()
ekran.keypad(1)
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
curses.noecho()
boyutlar = ekran.getmaxyx()
ekran.nodelay(1)
bold = 0
reverse = 0
b = [curses.A_NORMAL, curses.A_BOLD]
r = [curses.A_NORMAL, curses.A_REVERSE]
g = 0
q = -1
x, y = 0, 0
while q != ord("q"):
    ekran.clear()
    ekran.addstr(y, x, "hello world!",
                 curses.color_pair(g)| b[bold] | r[reverse])
    ekran.move(boyutlar[0] -1, boyutlar[1] - 1)
    ekran.refresh()
    q = ekran.getch()
    if q in range(48, 52):
        g = int(chr(q))
    elif q == 98:
        bold = 1 - bold
    elif q == 114:
        reverse = 1 - reverse
    if q == curses.KEY_UP and y > 0:
        y -= 1
    elif q == curses.KEY_DOWN and y < boyutlar[0] - 1:
        if y == boyutlar[0] - 2 and x == boyutlar[1] - \
                len("hello world!"):
            pass
        else:
            y += 1
    elif q == curses.KEY_LEFT and x > 0:
        x -= 1
    elif q == curses.KEY_RIGHT and x < boyutlar[1] - len("hello world!"):
        if y == boyutlar[0] - 1 and x == boyutlar[1] - \
                len("hello world!") - 1:
            pass
        else:
            x += 1
    time.sleep(0.05)
curses.endwin()
