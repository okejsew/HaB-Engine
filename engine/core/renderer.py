from typing import Optional

from engine.base.cmp.texture import Texture
from engine.base.scene import Scene
from engine.tools.console import set_point
from engine.tools.debug import Debug
from engine.tools.render import Renderer


class ObjectRenderer:
    scene: Optional[Scene] = None

    @staticmethod
    def setup(scene: Scene):
        ObjectRenderer.scene = scene
        Renderer.register(ObjectRenderer.render)

    @staticmethod
    def render_objects():
        ObjectRenderer.scene.camera.update()
        objects_to_draw = [obj for obj in ObjectRenderer.scene.objects if obj.visible]
        for obj in objects_to_draw:
            texture = obj.get_component(Texture)
            if not texture: continue
            for point in texture.get():
                if not ObjectRenderer.scene.camera.in_region(point):
                    continue
                set_point(point.offset - ObjectRenderer.scene.camera.region[0], point.sign)

    @staticmethod
    def render_info():
        camera_region = ObjectRenderer.scene.camera.region
        Debug.log('camera_position', f'Позиция камеры: {ObjectRenderer.scene.camera.transform.position}')
        Debug.log('camera_region', f'Регион камеры: {camera_region[0]} - {camera_region[1]}')
        Debug.log('scene_objects', f'Объектов на сцене: {len(ObjectRenderer.scene.objects)}')

    @staticmethod
    def render():
        ObjectRenderer.render_objects()
        ObjectRenderer.render_info()
