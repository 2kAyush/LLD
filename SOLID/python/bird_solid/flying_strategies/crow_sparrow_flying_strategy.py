from interfaces.flying_behaviour import FlyingBehaviourInterface

class CrowSparrowFlyingBehaviour(FlyingBehaviourInterface):
    def make_fly(self, name, _type):
        print(f"Common flying ({name}) of type: {_type} ")
