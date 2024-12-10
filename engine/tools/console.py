import curses
import time
from copy import deepcopy
from typing import Callable

import _curses
from threading import Thread

max_y, max_x = 0, 0
window: _curses.window
prev_buffer: list[list[str]]
buffer: list[list[str]]
drawers: list[Callable] = []


def __init__():
    global window, buffer, max_y, max_x, prev_buffer
    window = curses.initscr()
    window.nodelay(True)
    curses.raw()
    curses.cbreak()
    curses.curs_set(0)
    max_y, max_x = window.getmaxyx()
    buffer = [[' ' for _ in range(max_x)] for _ in range(max_y - 1)]
    prev_buffer = deepcopy(buffer)


def clear():
    global prev_buffer
    prev_buffer = deepcopy(buffer)
    for y, line in enumerate(buffer):
        for x, char in enumerate(buffer[y]):
            buffer[y][x] = ' '


def register(drawer: Callable):
    if drawer not in drawers:
        drawers.append(drawer)


def addstr(y: int, x: int, text: str):
    for _x, char in enumerate(text):
        if _x + x < max_x:
            addch(y, x + _x, char)


def addch(y: int, x: int, sign: str):
    if y < len(buffer) and x < len(buffer[y]):
        buffer[y][x] = sign


fps = 0

def render():
    global fps

    start = time.perf_counter()
    for drawer in drawers: drawer()

    for y, line in enumerate(buffer):
        try:
            line = ''.join(line)
            if y == 29: line = line[:-1]
            window.addstr(y, 0, line)
        except Exception as ex:
            window.addstr(0, 1, f'Errore: y={y}, {ex}')
    window.addstr(0, 0, f'Frames per second ≈ {fps}')
    window.refresh()
    clear()

    delta = time.perf_counter() - start
    fps = round(1 / delta, 2) if delta != 0 else fps
