#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses

screen = curses.initscr()
screen.keypad(1)
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
curses.noecho()
dimensions = screen.getmaxyx()
q = -1
x, y = 0, 0
xy = []
characters = []


def add_char(chr, num1, num2):
    global x, y
    screen.addstr(y, x, chr, curses.color_pair(1))
    x += 1
    characters.remove(num1)
    characters.remove(num2)


while q != 27:
    q = screen.getch()
    screen.refresh()
    characters.append(q)
    if dimensions[1] - x == 1:
        xy.append((y, x - 1))
        y += 1
        x = 0
    if q == 263:
        if x == 0:
            if y != 0:
                y -= 1
                try:
                    x = xy[len(xy) - 1][1]
                    xy.pop(len(xy) - 1)
                except IndexError:
                    x = dimensions[1] - 1
                screen.delch(y, x)
            else:
                pass
        else:
            screen.delch(y, x - 1)
            x -= 1
    elif q == 10:
        xy.append(curses.getsyx())
        screen.addstr(y, x, chr(10), curses.color_pair(1))
        y += 1
        x = 0
    elif q == 261:
        if dimensions[1] - x == 1:
            y += 1
            x = 0
        else:
            x += 1
            screen.addstr(y, x, "", curses.color_pair(1))
    elif q == 260:
        if x == 0:
            if y != 0:
                y -= 1
                x = 78
            else:
                pass
        else:
            x -= 1
            screen.addstr(y, x, "", curses.color_pair(1))
    elif q == 259:
        if y != 0:
            y -= 1
            screen.addstr(y, x, "", curses.color_pair(1))
        else:
            pass
    elif q == 258:
        if y != dimensions[0] - 1:
            y += 1
            screen.addstr(y, x, "", curses.color_pair(1))
        else:
            pass
    elif q == 195:
        screen.addstr(y, x, "", curses.color_pair(1))
    elif q == 196:
        screen.addstr(y, x, "", curses.color_pair(1))
    elif q == 197:
        screen.addstr(y, x, "", curses.color_pair(1))
    elif q == 167:
        add_char("\u00e7", 195, 167)
    elif q == 159:
        if 196 in characters:
            add_char("\u011f", 196, 159)
        elif 197 in characters:
            add_char("\u015f", 197, 159)
    elif q == 177:
        add_char("\u0131", 196, 177)
    elif q == 182:
        add_char("\u00f6", 195, 182)
    elif q == 188:
        add_char("\u00fc", 195, 188)
    elif q == 135:
        add_char("\u00c7", 195, 135)
    elif q == 158:
        if 196 in characters:
            add_char("\u011e", 196, 158)
        elif 197 in characters:
            add_char("\u015e", 197, 158)
    elif q == 176:
        add_char("\u0130", 196, 176)
    elif q == 150:
        add_char("\u00d6", 195, 150)
    elif q == 156:
        add_char("\u00dc", 195, 156)
    else:
        screen.addstr(y, x, chr(q), curses.color_pair(1))
        x += 1
curses.endwin()
