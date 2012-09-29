
import os

USAKEY = str(os.environ.get('USA_SECRET', 'Insert Key Here'))

def usakey():
    return USAKEY
