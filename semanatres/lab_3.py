#-------------------------
#person

#dni: int
#name: str
#lastname: int
#role:int
#-----------------------

from faker import Faker
import random

fake = Faker()
people_list=[]

def generate_people(num_people: int):

   
    for i in range(num_people):
        person = {
            "dni": i + 1,
            "name": fake.first_name(),
            "lastname": fake.last_name(),
            "role": random.randint(1,3)

        }
        people_list.append(person)
    
    return people_list

def select_role():
    for person in people_list:
        if(person["role"] == 1):
            person["role"] = "administrativo"
        elif(person["role"] == 2):
            person["role"] = "profesor"
        else:
            person["role"]= "estudiante"

def match_role():
    for person in people_list:
        match person["role"]:
            case 1:
                person["role"]= "estudiante"
            case 2:
                person["role"]= "profesor"
            case 3:
                person["role"]= "estudiante"


def print_people():
    for person in people_list:
        print(person)



number=int(input("por favor ingrese la cantidad de usuarios:\n"))
generate_people(number)
select_role()
match_role()
print_people()

