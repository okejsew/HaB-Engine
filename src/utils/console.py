import curses

import _curses

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
