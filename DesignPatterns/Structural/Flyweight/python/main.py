from typing import List

from Bullet import Bullet, BulletType
from BulletRegistry import BulletRegistry
from FlyingBullet import FlyingBullet

if __name__ == "__main__":
    bullet_7 = Bullet(7.62, 20, [7,6,2], BulletType.MM_762)
    bullet_5 = Bullet(5.56, 10, [5,5,6], BulletType.MM_556)
    bullet_9 = Bullet(9.12, 30, [9,1,2], BulletType.MM_912)

    bullet_registry = BulletRegistry()
    bullet_registry.register_bullet(BulletType.MM_556, bullet_5)
    bullet_registry.register_bullet(BulletType.MM_762, bullet_7)
    bullet_registry.register_bullet(BulletType.MM_912, bullet_9)

    bullet_list_7: List[FlyingBullet] = []
    for _ in range(4):
        bullet_list_7.append(FlyingBullet(300, "0,0,0", bullet_registry.get_bullet(BulletType.MM_762)))

    bullet_list_5: List[FlyingBullet] = []
    for _ in range(4):
        bullet_list_5.append(FlyingBullet(300, "0,0,0", bullet_registry.get_bullet(BulletType.MM_556)))

    bullet_list_9: List[FlyingBullet] = []
    for _ in range(4):
        bullet_list_9.append(FlyingBullet(300, "0,0,0", bullet_registry.get_bullet(BulletType.MM_912)))

    for i in bullet_list_5:
        print("5: ", id(i.bullet))

    for i in bullet_list_7:
        print("7: ", id(i.bullet))

    for i in bullet_list_9:
        print("9: ", id(i.bullet))