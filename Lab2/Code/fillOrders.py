from database import async_session_factory, session_factory
from ORM import User, Address, Orders
from sqlalchemy import select
from sqlalchemy.orm import selectinload
import random


with session_factory() as session:
    
    stmt = select(User).options(selectinload(User.addresses))
    results = session.execute(stmt).scalars().all()
    
    for user in results:
        price = random.randint(1, 10000)
        quantity = random.randint(1, 200)
        name = random.randint(1, 10)
        for i, user_address in enumerate(user.addresses):
            order = Orders(
                user_id=user.id,
                address_id=user_address.id,
                product_name=f"{name}",
                product_price=price,
                quantity=quantity
            )
            session.add(order)
    session.commit()
    