import re

class EmailAccount:
    def __init__(self,email,password) -> None:
        self.__email = email
        self.__password =password
        self.__user ={}

    
    def is_valid_email(email):
        email_regex = r'^[\w.+-]+@[\w]+\.[a-zA-Z0-9-.]+$'
        return True if re.match(email_regex, email) else False
        
    @property
    def email(self):
        return self.__email
    @property
    def password(self):
        self.__password

    @password.getter
    def password(self):
        return '*'*len(self.__password)

    
    @email.setter
    def set_email(self,email):
        
        if not EmailAccount.is_valid_email(email):
            raise ValueError("email and password cannot be empty.")

        self.__email=email

    @password.setter
    def set_password(self,password):
        if not password:
            raise ValueError("password cannot be empty.")
        self.__password = password
        return f"{password}"

    
    def __str__(self) -> str:
        return f'{self.email} with {self.password}'
    


user1 = EmailAccount('ali123@gmail.com','123')
user1.set_email="hasan@gmail.com"
user1.set_password="45667576"

print(user1)