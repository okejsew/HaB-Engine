import curses

from engine.tools.console import window


class Report:
    def __init__(self, color: int, message: str):
        self.color = color
        self.message = message


class Debug:
    stack: list[Report] = []
    updates: int = 0

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
    def render():
        for i, report in enumerate(Debug.stack):
            window.addstr(i, 0, report.message, report.color)

    @staticmethod
    def update():
        Debug.updates += 1
        if Debug.updates == 300:
            if Debug.stack:
                Debug.stack.pop(0)
            Debug.updates = 0
