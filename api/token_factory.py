import random
import string

class TokenFactory:

    @classmethod
    def generate_token(cls) -> str:
        rand = [random.choice(string.ascii_letters + string.digits) for i in range(30)]
        return ''.join(rand)