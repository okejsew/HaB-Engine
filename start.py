import curses
import time

size = 0


def main(window: curses.window):
    global size
    max_y, max_x = window.getmaxyx()
    for y in range(max_y):
        for x in range(max_x):
            window.addch(y, x, '@')
            window.refresh()
            time.sleep(0.005)
    window.getch()


curses.wrapper(main)
print(f'{size=}')
input()
