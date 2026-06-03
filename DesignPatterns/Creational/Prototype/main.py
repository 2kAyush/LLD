from BirdRegistry import BirdRegistry
from Pigeon import Pigeon


bird_reg = BirdRegistry()

big_pigeon  = Pigeon("Big", 2, 25, 12)
bird_reg.add_obj("big_pigeon", big_pigeon)

small_pigeon  = Pigeon("small", 0.5, 12, 2)

bird_reg.add_obj("small_pigeon", small_pigeon)

small_pigeon2 = bird_reg.get_new_obj("small_pigeon")

print(small_pigeon.__dict__, small_pigeon2.__dict__)