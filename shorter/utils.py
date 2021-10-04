from random import choices
from string import ascii_letters, digits


def create_random_string():
    """
    Creates a random string (length : 8)
    """
    return "".join(choices(ascii_letters + digits, k=8))


def create_random_password():
    """
    Creates a random password (length : 6) just digits
    """
    return "".join(choices(digits, k=6))
