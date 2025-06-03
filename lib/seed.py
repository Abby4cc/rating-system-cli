from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Product, Rating

def seed():
    engine = create_engine('sqlite:///e_product_rating.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        users_data = [
            {'username': 'abby', 'email': 'abby@gmail.com'},
            {'username': 'linda', 'email': 'linda@gmail.com'}
        ]

        for user_info in users_data:
            existing_user = session.query(User).filter_by(email=user_info['email']).first()
            if not existing_user:
                user = User(**user_info)
                session.add(user)
            else:
                print(f"User with email {user_info['email']} already exists.")

        session.commit()

        user1 = session.query(User).filter_by(email='abby@gmail.com').first()
        user2 = session.query(User).filter_by(email='linda@gmail.com').first()

        products_data = [
            {'name': 'Laptop', 'description': 'A high-performance laptop.'},
            {'name': 'Smartphone', 'description': 'A latest model smartphone.'}
        ]

        for product_info in products_data:
            existing_product = session.query(Product).filter_by(name=product_info['name']).first()
            if not existing_product:
                product = Product(**product_info)
                session.add(product)
            else:
                print(f"Product '{product_info['name']}' already exists.")


        session.commit()

        product1 = session.query(Product).filter_by(name='Laptop').first()
        product2 = session.query(Product).filter_by(name='Smartphone').first()

        ratings_data = [
            {'user_id': user1.id, 'product_id': product1.id, 'score': 5, 'comment': 'Excellent!'},
            {'user_id': user2.id, 'product_id': product2.id, 'score': 4, 'comment': 'Very good.'}
        ]

        for rating_info in ratings_data:
            existing_rating = session.query(Rating).filter_by(
                user_id=rating_info['user_id'],
                product_id=rating_info['product_id']
            ).first()
            if not existing_rating:
                rating = Rating(**rating_info)
                session.add(rating)
            else:
                print(f"Rating by user {rating_info['user_id']} for product {rating_info['product_id']} already exists.")

        session.commit()
        print("Seeding completed successfully.")

    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    seed()
