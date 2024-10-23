from src.components.texture import Texture, Point
from src.base.object import BaseObject
from src.utils.vector import Vector2


class Rectangle(BaseObject):
    def __init__(self, size_x: int = 3, size_y: int = 3, sign: str = '@'):
        """
        Прямоугольник\n
        Статичный (Не меняется динамически в зависимости
        от своих размеров (печалька))

        :param size_x: - Ширина прямоугольника
        :param size_y: - Высота прямоугольника
        :param sign: - Какими знаками будет заполнена текстура
        """
        super().__init__()
        self.name = 'Rectangle'
        self.add_component(self.generate_texture(size_x, size_y, sign))

    @staticmethod
    def generate_texture(size_x: int, size_y: int, sign: str = '@') -> Texture:
        """
        Генерация текстуры прямоугольника\n
        Размеры и знак это понятно, если надо какие то свои знаки, пишите сами свои прямоугольники\n
        Кстати, статичный метод, так что вы можете просто из класса его вызывать\n
        Возвращает компонент Texture наполненый точками в виде прямоугольника\n
        """
        texture = Texture()
        start_y = -round(size_y / 2)
        end_y = size_y + start_y

        start_x = -round(size_x / 2)
        end_x = size_x + start_x

        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                texture.points.append(Point(sign, Vector2(x, y)))
        return texture
