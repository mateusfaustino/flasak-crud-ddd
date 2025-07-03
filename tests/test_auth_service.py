import jwt
from flask import Flask

from app.services.auth_service import AuthService
from app.domain.entities import User
from app.domain.repositories import UserRepositoryInterface


class FakeUserRepository(UserRepositoryInterface):
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def get_by_username(self, username: str):
        for user in self.users.values():
            if user.username == username:
                return user
        return None

    def add(self, user: User) -> None:
        if user.id is None:
            user.id = self.next_id
            self.next_id += 1
        self.users[user.id] = User(
            id=user.id,
            username=user.username,
            password_hash=user.password_hash,
        )


def create_service():
    repo = FakeUserRepository()
    service = AuthService(repo)
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test-secret'
    return service, repo, app


def test_register_and_authenticate():
    service, repo, app = create_service()
    with app.app_context():
        user = service.register('bob', 'pass')
        assert user.id == 1
        assert repo.get_by_username('bob') is not None
        assert user.password_hash != 'pass'

        token = service.authenticate('bob', 'pass')
        assert token
        payload = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        assert payload['sub'] == user.id

        assert service.authenticate('bob', 'wrong') is None
        assert service.register('bob', 'pass') is None
