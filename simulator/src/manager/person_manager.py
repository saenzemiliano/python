from src.exeption.business_exception import BusinessError

class PersonManager(object):
    class __PersonManager:
        def __init__(self):
            self.persons = []

        def remove(self, index):
            return self.persons.pop(index)

        def  add(self, person):
            if self.exist(person):
                raise BusinessError('ERROR: Person already exists '+ '[Name: ' + person.name + ']' )
            self.persons.append(person)

        def  exist(self, person):
            for person_ in self.persons:
                if person_.name == person.name:
                    return True
            return False
    
    instance = None

    def __new__(cls): # __new__ always a classmethod
        if not PersonManager.instance:
            PersonManager.instance = PersonManager.__PersonManager()
        return PersonManager.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)