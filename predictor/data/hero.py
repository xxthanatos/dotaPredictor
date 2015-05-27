class Hero:

    def __init__(self, id, name, heroes):
        if(id is None and name is None):
            raise LookupError("must specify a name or id for a hero")

        self.id = id
        self.name = name

    def get_id_from_name(name):
        pass

    def get_name_from_id(id):
        pass
