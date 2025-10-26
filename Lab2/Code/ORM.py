from sqlalchemy.orm import declarative_base, mapped_column, relationship, Mapped
from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import ForeignKey


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)
    description: Mapped[str] = mapped_column(nullable=True, default="No description provided.")

    addresses = relationship("Address", back_populates="user")
    orders = relationship("Orders", back_populates="user")


class Address(Base):
    __tablename__ = 'addresses'

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'), nullable=False)
    street: Mapped[str] = mapped_column(nullable=False)
    city: Mapped[str] = mapped_column(nullable=False)
    state: Mapped[str] = mapped_column()
    zip_code: Mapped[str] = mapped_column()
    country: Mapped[str] = mapped_column(nullable=False)
    is_primary: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)

    user = relationship("User", back_populates="addresses")
    orders = relationship("Orders", back_populates="addresses")
    

class Orders(Base):
    __tablename__ = "orders"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    address_id: Mapped[UUID] = mapped_column(ForeignKey("addresses.id"), nullable=False)
    
    product_name: Mapped[str] = mapped_column(nullable=False)
    product_price: Mapped[float] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(default=1)
    
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    user = relationship("User", back_populates="orders")
    addresses = relationship("Address", back_populates="orders")