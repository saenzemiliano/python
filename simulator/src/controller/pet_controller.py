from src.manager.person_manager import PersonManager
from src.manager.pet_manager import PetManager
from src.model.cat import Cat
from src.model.dog import Dog
from src.model.pet import Pet


def pet_create(name):
    PetManager().add(Pet(name))


def pet_find_by_name(name):
    return PetManager().find(name)

def pet_remove_by_name(name):
    pass

def pet_add(name):
    pass

def pet_cut_hair(name):
    pet = pet_find_by_name(name)
    pet.cutHair()


def pet_feed(name):
    pet = pet_find_by_name(name)
    pet.feed()


def pet_list():
    for pet in PetManager().pets:
        print(pet)