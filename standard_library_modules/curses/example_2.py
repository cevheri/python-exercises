#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time

ekran = curses.initscr()
curses.noecho()
boyutlar = ekran.getmaxyx()
ekran.nodelay(1)
q = -1
x, y = 0, 0
while q != ord("q"):
    ekran.clear()
    ekran.addstr(y, x, "hello world!", curses.A_BOLD)
    ekran.refresh()
    q = ekran.getch()
    if q == ord("w") and y > 0:
        y -= 1
    elif q == ord("s") and y < boyutlar[0] - 1:
        y += 1
    elif q == ord("a") and x > 0:
        x -= 1
    elif q == ord("d") and x < boyutlar[1] - len("hello world!") - 1:
        x += 1
    time.sleep(0.05)
curses.endwin()
