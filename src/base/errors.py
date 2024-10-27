import curses


class Error:
    def __init__(self, *args):
        # from src.engine import Engine
        # Engine.close_threads()
        curses.endwin()
        input(f'{self.__class__.__name__}: {"".join(args)}', )
        exit()


class ComponentError(Error): ...


class SceneError(Error): ...


class ObjectError(Error): ...


class EngineError(Error): ...


class MissingOwnerError(ComponentError):
    def __init__(self, func, component):
        super().__init__(f'\nОшибка во время выполнения: {func.__name__}'
                         f'\nНет владельца для: {component}')


class ComponentNotFound(ObjectError):
    def __init__(self, t, obj):
        super().__init__(f'\nПоиск компонента типа {t} в объекте {obj} не дал результатов')


class MissingSceneError(EngineError):
    def __init__(self):
        super().__init__(f'\nОтсутствует сцена, работа движка невозможна')


class ObjectAlreadyAdded(SceneError):
    def __init__(self, obj, scene):
        super().__init__(f'\nОбъект {obj} уже добавлен на сцену {scene}')


class ObjectNotFound(SceneError):
    def __init__(self, obj, scene):
        super().__init__(f'\nПоиск объекта {obj} в сцене {scene} не дал результатов')


class TextureFileSyntaxIncorrect(ComponentError):
    def __init__(self, line):
        super().__init__(f'\nОшибка парсинга файла текстуры на этом месте: {line}')


class AnimationFileSyntaxIncorrect(ComponentError):
    def __init__(self, line):
        super().__init__(f'\nОшибка парсинга файла анимации на этом месте: {line}')


class MissingCameraOnScene(EngineError):
    def __init__(self, scene):
        super().__init__(f'Отсутствует камера для рендеринга на сцене: {scene}')
