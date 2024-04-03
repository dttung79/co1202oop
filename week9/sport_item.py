class SportItem:
    def __init__(self, id, name, branch, price):
        self._id = id
        self._name = name
        self._branch = branch
        self._price = price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID must be a positive integer.")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def branch(self):
        return self._branch

    @branch.setter
    def branch(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Branch must be a non-empty string.")
        self._branch = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not (isinstance(value, int) or isinstance(value, float)) or value < 0:
            raise ValueError("Price must be a non-negative number.")
        self._price = value
