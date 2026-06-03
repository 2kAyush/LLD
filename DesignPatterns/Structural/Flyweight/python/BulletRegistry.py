from Bullet import BulletType, Bullet

class BulletRegistry:
    def __init__(self):
        self.bullet_map = {}

    def register_bullet(self, bullet_type: BulletType, bullet: Bullet):
        self.bullet_map[bullet_type] = bullet

    def get_bullet(self, bullet_type: BulletType):
        return self.bullet_map[bullet_type]
