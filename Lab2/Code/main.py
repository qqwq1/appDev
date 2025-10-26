from database import async_session_factory, session_factory
from ORM import User, Address


with session_factory() as session:
    user1 = User(username="john_doe", email="john@example.com")
    user2 = User(username="ivan_ivanov", email="ivan@example.com")
    user3 = User(username="alex_cool", email="alex@example.com")
    user4 = User(username="ariana_grande", email="ariana@example.com")
    user5 = User(username="user5_lastname", email="user5@example.com")
    
    session.add_all([user1, user2, user3, user4, user5])
    session.commit()  
    
  
    address1 = Address(
        user_id=user1.id,  # Связь с user1
        street="123 Main St",
        city="New York",
        state="NY",
        zip_code="10001",
        country="USA"
    )
    address2 = Address(
        user_id=user2.id,  # Связь с user2
        street="456 Elm St",
        city="Los Angeles",
        state="CA",
        zip_code="90210",
        country="USA"
    )
    
    address3 = Address(
        user_id=user3.id,  # Связь с user3
        street="789 Oak St",
        city="Chicago",
        state="IL",
        zip_code="60601",
        country="USA"
    )
    address4 = Address(
        user_id=user4.id,  # Связь с user4
        street="321 Pine St",
        city="Houston",
        state="TX",
        zip_code="77001",
        country="USA"
    )
    address5 = Address(
        user_id=user5.id,  # Связь с user5
        street="654 Maple St",
        city="Phoenix",
        state="AZ",
        zip_code="85001",
        country="USA"
    )

    session.add_all([address1, address2, address3, address4, address5])  # Добавьте все адреса
    session.commit()

