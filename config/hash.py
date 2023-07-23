from passlib.context import CryptContext


class Hash():
    pws_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def bcrypt(self, password):
        return self.pws_cxt.hash(password)

    def verify(self, hashed_password, plain_password):
        return self.pws_cxt.verify(plain_password, hashed_password)
