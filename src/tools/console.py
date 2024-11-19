import curses

import _curses

from src.base.utils.vector import Vector2

window: _curses.window = curses.initscr()
window.border(0)
window.nodelay(True)
curses.nocbreak()
curses.noecho()
curses.curs_set(0)
curses.start_color()
curses.mousemask(curses.REPORT_MOUSE_POSITION)
curses.start_color()
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)


def set_point(pos: Vector2, sign: str):
    try:
        window.addch(pos.y, pos.x, sign)
    finally:
        ...


def color(num: int):
    return curses.color_pair(num)
