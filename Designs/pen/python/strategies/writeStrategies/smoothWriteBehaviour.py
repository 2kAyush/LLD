from .writeBehaviour import WriteBehaviour

class SmoothWriteBehaviour(WriteBehaviour):
    def write(self):
        print("Writing smoothly")