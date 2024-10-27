from src.base.object import BaseObject
from src.base.scene import Scene
from src.components.rigidbody import Rigidbody
from src.components.texture import Texture
from src.engine import Engine
from src.utils.vector import Vector2

# Создание сцены и настройка движка
scene = Scene()
Engine.current_scene = scene
Engine.debug_mode = True

# Создание объекта и установка параметров

obj = BaseObject()
obj.transform.position = Vector2(50, 10)

# Добавляем объект на сцену
scene.add(obj)

# Настраиваем и добавляем компоненты
obj.add_component(Texture())

obj.get_component(Texture).load('src/assets/textures/test.tx')

obj.add_component(Rigidbody())

# Запускаем движок
Engine.run()
