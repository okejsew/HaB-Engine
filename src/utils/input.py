from src.utils.console import window


class Input:
    @staticmethod
    def get_key() -> int: return window.getch()