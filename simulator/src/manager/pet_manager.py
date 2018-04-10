from src.exeption.business_exception import BusinessError

class PetManager(object):
    class __PetManager:
        def __init__(self):
            self.pets = []

        def remove(self, index):
            return self.pets.pop(index)

        def  add(self, pet):
            if self.exist(pet):
                raise BusinessError('ERROR: Pet already exists '+ '[Name: ' + pet.name + ']'  )
            self.pets.append(pet)

        def  exist(self, pet):
            for pet_ in self.pets:
                if pet_.name == pet.name:
                    return True
            return False

        def  find(self, name):
            for pet_ in self.pets:
                if pet_.name == name:
                    return pet_
            raise BusinessError('ERROR: Pet is not exists '+ '[Name: ' + name + ']'  )
        
    
    instance = None

    def __new__(cls): # __new__ always a classmethod
        if not PetManager.instance:
            PetManager.instance = PetManager.__PetManager()
        return PetManager.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)