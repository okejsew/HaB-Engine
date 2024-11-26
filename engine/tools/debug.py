from engine.tools.console import window, Console


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
    def setup():
        Debug.__max_y = window.getmaxyx()[0]
        Console.register(Debug.render)

    @staticmethod
    def info(message: str):
        Debug.stack.append(Report('(INFO)', message))

    @staticmethod
    def warn(message: str):
        Debug.stack.append(Report('{WARN}', message))

    @staticmethod
    def error(message: str):
        Debug.stack.append(Report('[ ERROR ]', message))

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
        if Debug.tick == 2500:
            Debug.tick = 0
            if Debug.stack:
                Debug.stack.pop(-1)
