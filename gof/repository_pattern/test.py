import pytest
from entity import LocalUser
from repository import LocalRepository
from repository import NotFoundException


def test_local_factory():
    # Build factory
    users = [
        LocalUser(id_=1, name="FirstUser"),
        LocalUser(id_=2, name="SecondUser")
    ]
    factory = LocalRepository(users=users)

    # Found case
    user = factory.get_user(id_=1)
    assert user.id_ == 1
    assert user.name == "FirstUser"

    # NotFound case
    with pytest.raises(NotFoundException):
        user = factory.get_user(id_=3)
