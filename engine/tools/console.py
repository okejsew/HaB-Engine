import curses
from typing import Callable

import _curses

from engine.common.vector import Vector2

window: _curses.window = curses.initscr()
window.border(0)
window.nodelay(True)
window.keypad(True)
curses.nocbreak()
curses.noecho()
curses.curs_set(0)
curses.mousemask(curses.REPORT_MOUSE_POSITION)


def set_point(pos: Vector2, sign: str):
    max_y, max_x = window.getmaxyx()
    if ((0 <= pos.x < max_x and 0 <= pos.y < max_y) and
            not (pos.y == max_y - 1 and pos.x == max_x - 1)):
        window.addch(pos.y, pos.x, sign[0])


def color(num: int):
    return curses.color_pair(num)


class Console:
    fps = 0.0
    listeners: list[Callable] = []

    @staticmethod
    def register(listener: Callable):
        Console.listeners.append(listener)

    @staticmethod
    def update():
        window.clear()
        for listener in Console.listeners:
            listener()
        window.refresh()

    @staticmethod
    def end():
        Console.listeners.clear()
        window.clear()
        curses.endwin()
