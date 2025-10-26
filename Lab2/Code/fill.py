from database import async_session_factory, session_factory
from ORM import User, Address, Orders
from sqlalchemy import select
from sqlalchemy.orm import selectinload
import random


with session_factory() as session:
    # Берём 5 пользователей и их адреса (по одному адресу на пользователя)
    users = session.query(User).all()
    desc = ["Updated user info", "Regular user", "Premium member", "New user", "Loyal customer"]
    for user in users:
        user.description = random.choice(desc)
        session.commit()
