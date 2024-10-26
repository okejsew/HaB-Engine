from src.api import *


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
obj.add_component(BasicMovement())
obj.add_component(Animator())
obj.get_component(Animator).load('src/assets/animations/walking.an')
obj.get_component(Animator).loop = -1
obj.get_component(Animator).start()

# Запускаем движок
Engine.run()
