# HaB-Engine
Консольный движок, основанный на python и windows-curses.
Фичи обычных движок в консоли: физика, скрипты, текстуры и много другое.
Система текстур состоящая из точек. В общем круть.


## Создаем сцену (место, где будут хранится все объекты):
```python
from src.base.scene import Scene

scene = Scene()
```

## Устанавливаем текущую сцену в движке, чтобы он обрабатывал именно ее:
```python
from src.base.scene import Scene
from src.engine import Engine

Engine.current_scene = Scene()
```

Можем включить debug mode, он будет показывать некоторые значение в левом верхнем углу экрана:
```python
from src.engine import Engine

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
from src.base.object import BaseObject

obj = BaseObject()

obj.name = 'My first Object'   # Имя объекта
obj.visible = False            # Его видимость (Если у него есть текстура конечно)
obj.position = Vector2(5, 10)  # Его положение в пространстве
```
Позиционирование:
```python
from src.utils.vector import Vector2
pos = Vector2(5, 10) # Вектор2 типа int, потому что мы в консольном мире
```
И так как тут всё немного по другому, чем ***меньше*** `y`, тем ***выше*** объект


## Компоненты
Всё строится на компонентах. 
Их можно добавлять, убирать, получать, получать все похожие.
Можно писать свои компоненты или наследоваться от готовых 
(Например от текстуры, и написать свою, которая будет менять от обстоятельств, например)

```python
from src.components.texture import Texture
from src.components.rigidbody import Rigidbody
from src.assets.scripts.test_script import CameraTracking

from src.base.object import BaseObject

obj = BaseObject()
obj.add_component(Texture())  # Текстура
obj.add_component(Rigidbody())  # Физика
obj.add_component(CameraTracking())  # Скрипт

# Аналогично, можно их получать и использовать
texture = obj.get_component(Texture)
texture.load('src/assets/textures/test.tx')
```