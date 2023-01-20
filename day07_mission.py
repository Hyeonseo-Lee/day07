#10.10

class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class Smartphone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.ring = Smartphone()

    def does(self):
        return (f'{self.laser.does()}, {self.claw.does()}, {self.ring.does()}')

a = Robot()
print(a.does())









