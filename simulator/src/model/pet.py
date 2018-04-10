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
        self.hair = 10
        self.hungry = 100
        self.state = PetStatus.GOOD

    def grunt(self):
        pass

    def weight(self):
        pass


    def __str__(self):
        return self.name + ' ' + '[' + str(self.state.name) + ']'
    def __unicode__(self):
        return '%d' % (self.name)