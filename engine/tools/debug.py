from dataclasses import dataclass

from engine.tools.console import window


@dataclass
class Report:
    type: str
    message: str


class Debug:
    __max_y = window.getmaxyx()[0]
    stack: list[Report] = []
    log_stack: dict[str, str] = {}
    tick = 0

    @staticmethod
    def add(report: Report):
        if len(Debug.stack) < 20:
            Debug.stack.append(report)

    @staticmethod
    def info(message: str):
        Debug.add(Report('(INFO)', message))

    @staticmethod
    def warn(message: str):
        Debug.add(Report('[WARN]', message))

    @staticmethod
    def error(message: str):
        Debug.add(Report('[ ERROR ]', message))

    @staticmethod
    def log(sender, message):
        Debug.log_stack[sender] = message

    @staticmethod
    def render():
        for i, report in enumerate(Debug.stack[:10]):
            window.addstr(i + 1, 1, f'{report.type} {report.message}')
        for i, (sender, message) in enumerate(Debug.log_stack.items()):
            window.addstr(Debug.__max_y - i - 2, 1, message)
        Debug.update()

    @staticmethod
    def update():
        Debug.tick += 1
        if Debug.tick == 3500:
            Debug.tick = 0
            if Debug.stack:
                Debug.stack.pop(0)
