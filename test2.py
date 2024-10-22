import curses
from curses import *

window = curses.initscr()
curses.start_color()
colors = [COLOR_WHITE, COLOR_BLACK, COLOR_BLUE, COLOR_GREEN, COLOR_RED, COLOR_YELLOW]
strs = {7: 'white', 0: 'black', 1: 'blue', 2: 'green', 4: 'red', 6: 'yellow'}
result = {}

def get_color_numbero(fg, bg):
    return (strs[fg] << 24) | (strs. << 16)

i = 1
for color1 in colors:
    for color2 in colors:
        curses.init_pair(i, color1, color2)
        result[(color1, color2)] = curses.color_pair(i)
        i += 1

window.addstr('Hello World', 436207616)
window.refresh()
window.getch()

curses.endwin()
print('fg', 'bg', 'code')
for pair, color in result.items():
    print(strs[pair[0]], strs[pair[1]], color)
input()