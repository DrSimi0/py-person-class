class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for person in people:
        for key, value in person.items():
            if key == "wife" and value is not None:
                persona_objetivo = Person.people[person["name"]]
                persona_objetivo.wife = Person.people[value]
            elif key == "husband" and value is not None:
                persona_objetivo = Person.people[person["name"]]
                persona_objetivo.husband = Person.people[value]

    return person_list
