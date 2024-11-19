from src.tools.console import window


class Input:
    @staticmethod
    def get_key() -> int:
        return window.getch()
