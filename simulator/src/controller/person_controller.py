from src.manager.person_manager import PersonManager
from src.manager.pet_manager import PetManager
from src.model.person import Person
from src.model.cat import Cat
from src.model.dog import Dog
from src.model.pet import Pet


def person_create(name, email):
    PersonManager().add(Person(name, email))


def person_find_by_name(name):
    return PetManager().find(name)

def person_find_by_email(email):
    pass

def person_remove_by_name(name):
    pass

def person_remove_by_email(email):
    pass

def person_add_pet(name_person, name_pet):
    pass

def person_remove_pet(name_oerson, name_pet):
    pass

def person_list():
    for person in PersonManager().persons:
        print(person)