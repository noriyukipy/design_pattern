class User:
    def __init__(self, id_, name):
        self._id_ = id_
        self._name = name

    @property
    def id_(self):
        return self._id_

    @property
    def name(self):
        return self._name
