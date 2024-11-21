import curses

from engine.tools.console import window


class Report:
    def __init__(self, color: int, message: str):
        self.color = color
        self.message = message


max_y, _ = window.getmaxyx()
class Debug:
    stack: list[Report] = []
    log_stack: dict[str, str] = {}
    tick: int = 0

    @staticmethod
    def info(message: str):
        Debug.stack.append(Report(curses.color_pair(4), message))

    @staticmethod
    def warn(message: str):
        Debug.stack.append(Report(curses.color_pair(3), message))

    @staticmethod
    def error(message: str):
        Debug.stack.append(Report(curses.color_pair(2), message))

    @staticmethod
    def log(sender, message):
        Debug.log_stack[sender] = message

    @staticmethod
    def render():
        for i, report in enumerate(Debug.stack[:10]):
            window.addstr(i + 1, 1, report.message, report.color)
        for i, (sender, message) in enumerate(Debug.log_stack.items()):
            window.addstr(max_y - i - 2, 1, message)

    @staticmethod
    def update():
        Debug.tick += 1
        if Debug.tick == 150:
            if Debug.stack:
                Debug.stack.pop(0)
            Debug.tick = 0
