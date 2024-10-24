from src.assets.objects.pospoint import PositionPoint
from src.assets.scripts.test_script import TestScript
from src.base.object import BaseObject
from src.components.rigidbody import Rigidbody
from src.components.texture import Texture
from src.utils.vector import Vector2
from src.base.scene import Scene
from src.engine import Engine

# Создание сцены и настройка движка
scene = Scene()
Engine.current_scene = scene
Engine.debug_mode = True

# Создание объекта и установка параметров
obj = BaseObject()
obj.position = Vector2(50, 10)

# Добавляем объект на сцену
scene.add(obj)

# Настраиваем и добавляем компоненты
t = Texture()
t.load('src/assets/textures/test.tx')

obj.add_component(t)
obj.add_component(Rigidbody())
obj.add_component(TestScript())

# Запускаем движок
Engine.run()
