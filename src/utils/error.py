class Errors:
    errors: list[str] = []
    updates: int = 0

    @staticmethod
    def add(error: str):
        Errors.errors.append(error)

    @staticmethod
    def update():
        Errors.updates += 1
        if Errors.updates == 300:
            if Errors.errors:
                Errors.errors.pop(0)
            Errors.updates = 0
