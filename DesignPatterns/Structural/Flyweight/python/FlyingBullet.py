from Bullet import Bullet

class FlyingBullet:
    def __init__(self, speed, co_ordinates, bullet: Bullet):
        self.speed = speed
        self.co_ordinates = co_ordinates
        self.bullet = bullet