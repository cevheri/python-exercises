#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import curses
import keyword

screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.noecho()
q = -1
chars = ""
while q != ord("q"):
    q = screen.getch()
    screen.addstr(chr(q), curses.color_pair(1))
    chars += chr(q)
    for kw in keyword.kwlist:
        regex1 = re.search("[^'\"]\s{}\s$".format(kw), chars)
        regex2 = re.search("^{}\s$".format(kw), chars)
        if regex1 or regex2:
            screen.addstr("{}{} ".format("\b" * (len(kw) + 1), kw),
                          curses.color_pair(2))
            chars = ""
curses.endwin()
