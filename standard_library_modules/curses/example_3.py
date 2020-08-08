#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time

ekran = curses.initscr()
boyutlar = ekran.getmaxyx()
ekran.nodelay(1)
q = -1
x, y = 0, 0
dusey, yatay = 1, 1
while q < 0:
    ekran.clear()
    ekran.addstr(y, x, "<<<    CEVHERİ    >>>", curses.A_BOLD)
    ekran.refresh()
    y += dusey
    x += yatay
    if y == boyutlar[0] - 1:
        dusey = -1
    elif y == 0:
        dusey = 1
    if x == boyutlar[1] - len("<<<    CEVHERİ    >>>") - 1:
        yatay = -1
    elif x == 0:
        yatay = 1
    q = ekran.getch()
    time.sleep(0.05)
curses.endwin()
