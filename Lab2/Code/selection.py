from sqlalchemy import select
from sqlalchemy.orm import selectinload
from database import session_factory
from ORM import User


print("Users with their addresses:")
with session_factory() as session:
    stmt = select(User).options(selectinload(User.addresses))
    results = session.execute(stmt).scalars().all()

    for user in results:
        print(f"User: {user.username}, Email: {user.email}")
        for address in user.addresses:
            print(f"  Address: {address.street}, {address.city}, {address.state}, {address.zip_code}, {address.country}")