import string
import random


def generate_random_record_locator(prefix=''):
    """
    The following function generates an RLOC in one of two ways:
    Legacy (prefix not specified): 6 random character RLOC
    Prefix != None: RLOC with the prefix and random characters making up the balance to 8 char
    """
    if prefix == '':
        size = 6
    else:
        size = 8 - len(prefix)

    chars = string.ascii_uppercase + string.digits
    return str.upper(prefix) + (''.join(random.choice(chars) for _ in range(size)))


def generate_random_id(prefix='', length=16):
    """
    The following function generates a random id taking in input a prefix and a length
    """
    if prefix == '':
        size = length
    else:
        size = length - len(prefix)

    chars = string.digits
    return str.upper(str(prefix)) + (''.join(random.choice(chars) for _ in range(size)))


def generate_random_ticket_number(prefix=''):
    """
    The following function generates a ticket number in one of two ways:
    Legacy (prefix not specified): 13 random digits
    Prefix != None: Ticket Number with the prefix (Airline code) and random digits making up the balance to 13 char
    """
    if prefix == '':
        size = 13
    else:
        size = 13 - len(prefix)

    chars = string.digits
    return str.upper(prefix) + (''.join(random.choice(chars) for _ in range(size)))