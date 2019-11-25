class NotFoundException(Exception):
    pass


class Repository:
    """Interface class"""
    def get_user(self, id_):
        raise NotImplementedError()


class LocalRepository(Repository):
    def __init__(self, users):
        self._users = users

    def get_user(self, id_):
        for user in self._users:
            if id_ == user.id_:
                return user
        raise NotFoundException()
