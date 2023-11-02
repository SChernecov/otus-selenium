import random

en_lowercase = 'abcdefghijklmnopqrstuvwxyz'
en_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def random_letters():
    letters = en_lowercase + en_uppercase
    return ''.join(random.choice(letters) for _ in range(10))


def random_email():
    user = ''.join(random.choice(en_lowercase))
    domain = ''.join(random.choice(en_lowercase))
    return f"{user}@{domain}.com"
