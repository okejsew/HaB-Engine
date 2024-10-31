from src.base.component import BaseComponent
from src.utils.vector import Vector2F


class Rigidbody(BaseComponent):
    def __init__(self):
        super().__init__()
        self.velocity: Vector2F = Vector2F()
        self.acceleration: Vector2F = Vector2F()
        self.force: Vector2F = Vector2F()

        self.mass = 1
        self.is_gravity = True
        self.gravity = 0.981
        self.max_fall_speed: float = 10

    def add_force(self, force: Vector2F):
        self.force += force

    def update(self, delta_time: float = 0.05):
        if self.is_gravity:
            self.add_force(Vector2F(0, self.gravity * self.mass))

        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration * delta_time

        if self.velocity.length() > self.max_fall_speed:
            self.velocity = self.velocity.normalized() * self.max_fall_speed

        self.owner.transform.translate(self.velocity * delta_time)
        self.force = Vector2F()
