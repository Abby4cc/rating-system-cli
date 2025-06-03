from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    ratings = relationship('Rating', back_populates='user')

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)

    ratings = relationship('Rating', back_populates='product')

    def __repr__(self):
        return f"<Product(name='{self.name}')>"

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    score = Column(Integer, nullable=False)
    comment = Column(Text)

    user = relationship('User', back_populates='ratings')
    product = relationship('Product', back_populates='ratings')

    def __repr__(self):
        return f"<Rating(user_id={self.user_id}, product_id={self.product_id}, score={self.score})>"
