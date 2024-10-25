from src.api import *

# Создание сцены и настройка движка
scene = Scene()
Engine.current_scene = scene
Engine.debug_mode = True

# Создание объекта и установка параметров
obj = PositionPoint()
other = BaseObject()
other.add_component(Texture())
other.get_component(Texture).load('src/assets/textures/test.tx')
other.position = Vector2(55, 15)
obj.position = Vector2(50, 10)

# Добавляем объект на сцену
scene.add(obj)
scene.add(other)

# Настраиваем и добавляем компоненты
t = Texture()
t.load('src/assets/textures/test.tx')

obj.add_component(t)
obj.add_component(Rigidbody())

ct = CameraTracking()
ct.target = obj
scene.camera.add_component(ct)


# Запускаем движок
Engine.run()
