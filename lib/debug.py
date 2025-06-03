import ipdb
from models import Base, User, Product, Rating

def debug_session():
    session = Session()
    ipdb.set_trace()
