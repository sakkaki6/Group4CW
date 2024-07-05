

from random import randint


class CredentialsManager:
    credentials = {}

    def __init__(self, username, password):
        self.id = randint(1, 1000)
        self.__username = username
        self.__password = password
        CredentialsManager.credentials[self.id] = self
# self.__credentials = {self}

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @password.getter
    def password(self):
        return '*'*len(self.__password)

    @password.setter
    def password(self, password):
        if not password:
            raise ValueError("Username and password cannot be empty.")
        self.__password = password
        return (f"Credentials set for user: {password}")

    @username.setter
    def username(self, username):
        if not username:
            raise ValueError("Username and password cannot be empty.")

        return (f"Credentials set for user: {username}")

   

    def __repr__(self) -> str:
        return f"user :{self.username}Password: {self.password}"


user1 = CredentialsManager('ali', '1230000')
user1.username='arash'
user1.password='987'
print(CredentialsManager.credentials[user1.id])


