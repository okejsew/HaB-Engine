from engine.tools.console import window


class Report:
    def __init__(self, _type: str, message: str):
        self.type = _type
        self.message = message

class Debug:
    __max_y = 0
    stack: list[Report] = []
    log_stack: dict[str, str] = {}
    tick = 0

    @staticmethod
    def setup(max_y: int):
        Debug.__max_y = max_y

    @staticmethod
    def info(message: str):
        Debug.stack.append(Report('INFO', message))

    @staticmethod
    def warn(message: str):
        Debug.stack.append(Report('!WARN!', message))

    @staticmethod
    def error(message: str):
        Debug.stack.append(Report('==!ERROR!==', message))

    @staticmethod
    def log(sender, message):
        Debug.log_stack[sender] = message

    @staticmethod
    def render():
        for i, report in enumerate(Debug.stack[:10]):
            window.addstr(i + 1, 1, f'[{report.type}] {report.message}')
        for i, (sender, message) in enumerate(Debug.log_stack.items()):
            window.addstr(Debug.__max_y - i - 2, 1, message)

    @staticmethod
    def update():
        Debug.tick += 1
        if Debug.tick == 2000:
            Debug.tick = 0
            Debug.stack.pop(-1)
