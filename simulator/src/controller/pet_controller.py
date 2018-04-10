from src.manager.person_manager import PersonManager
from src.manager.pet_manager import PetManager
from src.model.cat import Cat
from src.model.dog import Dog
from src.model.pet import Pet


def pet_create(name):
    PetManager().add(Pet(name))


def pet_find_by_name(name):
    pass

def pet_remove_by_name(name):
    pass

def pet_add(namePet):
    pass

def pet_cut_hair():
    pass


def pet_feed():
    pass


def pet_list():
    for pet in PetManager().pets:
        print(pet)