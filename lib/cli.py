from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Product, Rating
from helpers import display_menu

engine = create_engine('sqlite:///e_product_rating.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def register_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print(f"User '{username}' registered successfully.")

def add_product():
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    product = Product(name=name, description=description)
    session.add(product)
    session.commit()
    print(f"Product '{name}' added successfully.")

def rate_product():
    user_id = int(input("Enter your user ID: "))
    product_id = int(input("Enter product ID: "))
    score = int(input("Enter rating score (1-5): "))
    comment = input("Enter comment: ")
    rating = Rating(user_id=user_id, product_id=product_id, score=score, comment=comment)
    session.add(rating)
    session.commit()
    print("Rating submitted successfully.")

def view_products():
    products = session.query(Product).all()
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Description: {product.description}")

def view_ratings():
    ratings = session.query(Rating).all()
    for rating in ratings:
        print(f"User ID: {rating.user_id}, Product ID: {rating.product_id}, Score: {rating.score}, Comment: {rating.comment}")

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            add_product()
        elif choice == '3':
            rate_product()
        elif choice == '4':
            view_products()
        elif choice == '5':
            view_ratings()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
