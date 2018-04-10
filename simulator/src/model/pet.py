from enum import Enum, unique

@unique
class PetStatus(Enum):
    GOOD = 1
    EXCELLENT = 2
    BAD = 3
    AWFUL = 4

class Pet(object):
    def __init__(self, name):
        self.name = name
        self.hair = 100
        self.hungry = 100
        self.state = PetStatus.GOOD

    def grunt(self):
        pass

    def weight(self):
        pass

    def feed(self):
        self.hungry = self.hungry + 10 

    def cutHair(self):
        self.hair = self.hair - 10


    def __str__(self):
        return  '[Name: ' + self.name + ', State: ' + str(self.state.name) + ', Hair: ' + str(self.hair) + ', Hungry: ' + str(self.hungry) + ']'
    def __unicode__(self):
        return '%d' % (self.name)