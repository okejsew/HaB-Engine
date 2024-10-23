# HaB-Engine

## Создаем сцену (место, где будут хранится все объекты):
```python
from src.base.scene import Scene
scene = Scene()
```

## Устанавливаем текущую сцену в движке, чтобы он обрабатывал именно ее:
```python
from src.engine import Engine
Engine.current_scene = scene
```

Можем включить debug mode, он будет показывать некоторые значение в левом верхнем углу экрана:
```python
Engine.debug_mode = True
```

## Создаём объект:
```python
from src.base.object import BaseObject
obj = BaseObject()
```

У объектов есть некоторые параметры которые можно менять:
```python
from src.utils.vector import Vector2

obj.name = 'My first Object'   # Имя объекта
obj.visible = False            # Его видимость (Если у него есть текстура конечно)
obj.position = Vector2(5, 10)  # Его положение в пространстве
```
Позиционирование:
```python
pos = Vector2(5, 10) # Вектор2 типа int, потому что мы в консольном мире
```
И так как тут всё немного по другому, чем ***меньше*** `y`, тем ***выше*** объект

