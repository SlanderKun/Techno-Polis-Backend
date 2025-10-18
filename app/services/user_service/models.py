import enum
import sqlalchemy

import database.models


class UserRole(enum.Enum):
    university = "university"
    admin = "admin"
    company = "company"


class User(database.models.BaseTable):
    __tablename__ = 'users'

    role = sqlalchemy.Column(sqlalchemy.Enum(UserRole), nullable=False)
    email = sqlalchemy.Column(
        sqlalchemy.String(50),
        nullable=False,
        unique=True,
    )
    password_hash = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    external_id = sqlalchemy.Column(sqlalchemy.BigInteger, nullable=True)
