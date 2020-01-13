class Person:
    def __init__(self, id):
        self.id = id
        self.friends = list()

    @property
    def get_id(self):
        return self.id

    def add_friend(self, friend_id: int):
        self.friends.append(friend_id)


class Machine:
    def __init__(self, id):
        self.id = id
        self.id_to_person = dict()

    def get_person_with_id(self, person_id):
        return self.id_to_person.get(person_id)


class Server:
    def __init__(self, name):
        self.name = name
        self.id_to_machine = dict()
        self.person_to_machine = dict()

    def get_machine_id_for_person(self, id):
        return self.person_to_machine.get(id) if self.person_to_machine else None

    def get_machine_with_id(self, id):
        return self.id_to_machine.get(id) if self.id_to_machine else None

    def get_person_with_id(self, id):
        machine_id = self.get_machine_id_for_person(id)
        if machine_id is not None:
            machine = self.get_machine_with_id(machine_id)
            if machine is not None:
                return machine.get_persion_with_id(id)
        return None
