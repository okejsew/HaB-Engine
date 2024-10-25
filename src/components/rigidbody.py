from src.base.component import BaseComponent
from src.utils.vector import Vector2, Vector2F

class Rigidbody(BaseComponent):
    def __init__(self):
        super().__init__()
        self.velocity: Vector2F = Vector2F()            # Скорость
        self.acceleration: Vector2F = Vector2F()        # Ускорение
        self.force: Vector2F = Vector2F()               # Сила
        self.velocity_remainder: Vector2F = Vector2F()  # Остаток скорости для накопления

        self.mass = 1                       # Масса
        self.is_gravity = True              # Гравитация включена
        self.gravity = 0.981                # Сила гравитации
        self.max_fall_speed: float = 10     # Максимальная скорость падения

    def add_force(self, force: Vector2F):
        self.force += force

    def update(self, delta_time: float = 0.05):
        if self.is_gravity:
            self.add_force(Vector2F(0, self.gravity * self.mass))  # Применяем гравитацию

        self.acceleration = self.force / self.mass       # Ускорение: a = f / m
        self.velocity += self.acceleration * delta_time  # Скорость: v = v + a * delta_time

        # Ограничение скорости
        if self.velocity.length() > self.max_fall_speed:
            self.velocity = self.velocity.normalized() * self.max_fall_speed

        # Если остаток скорости > 0 но < 1, сохраняем его на след. шаг и добавляем там
        total_velocity: Vector2F = self.velocity * delta_time
        total_velocity += self.velocity_remainder
        int_velocity: Vector2 = total_velocity.to_int()
        self.velocity_remainder = total_velocity - int_velocity

        self.owner.position += int_velocity
        self.force = Vector2F()
