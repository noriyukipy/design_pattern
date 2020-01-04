class User:
    @property
    def id_(self):
        raise NotImplementedError()

    @property
    def name(self):
        raise NotImplementedError()


class LocalUser(User):
    def __init__(self, id_, name):
        self._id_ = id_
        self._name = name

    @property
    def id_(self):
        return self._id_

    @property
    def name(self):
        return self._name
