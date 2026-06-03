from enum import Enum

class BulletType(str, Enum):
    MM_556 = "5.56mm"
    MM_762 = "7.62mm"
    MM_912 = "9.12mm"


class Bullet:
    def __init__(self, radius: float, weight: float, image, bullet_type: BulletType):
        self.radius = radius
        self.weight = weight
        self.image = image
        self.bullet_type = bullet_type
