# curses module
# The curses module provides an interface to the curses library,
# the de-facto standard for portable advanced terminal handling.
#
# While curses is most widely used in the Unix environment,
# versions are available for Windows, DOS, and possibly other systems as well.
# This extension module is designed to match the API of ncurses,
# an open-source curses library hosted on Linux and the BSD variants of Unix.
#
# ref : https://docs.python.org/3/library/curses.html
# ref : https://python-istihza.yazbel.com/standart_moduller/curses.html

import curses
# stdscr = curses.initscr()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses

screen = curses.initscr()
dimensions = screen.getmaxyx()
screen.addstr(int(dimensions[0] / 2), int(dimensions[1] / 2 - 6), "hello world!",
              curses.A_BOLD)
screen.refresh()
screen.getch()
curses.endwin()

















