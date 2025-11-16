import random 
import string
from models import (insert_url)

def create_short_url(original_url, length=6):
    while True:
        short_code = ''.join((random.choice(string.ascii_letters + string.digits) for _ in range(length)))
        try:
            insert_url(original_url, short_code)
            return short_code
        except Exception as e:
            print(str(e))
    