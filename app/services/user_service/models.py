import enum

import database.models
import sqlalchemy
import sqlalchemy.orm


class UserRole(enum.Enum):
    university = "university"
    admin = "admin"
    company = "company"


class UserStatus(enum.Enum):
    pending = "pending"
    active = "active"
    inactive = "inactive"
    banned = "banned"


class User(database.models.Base):
    __tablename__ = "users"

    id: sqlalchemy.orm.Mapped[database.models.intpk]
    created_at: sqlalchemy.orm.Mapped[database.models.created_at]
    updated_at: sqlalchemy.orm.Mapped[database.models.updated_at]

    role = sqlalchemy.Column(sqlalchemy.Enum(UserRole), nullable=True)
    status = sqlalchemy.Column(
        sqlalchemy.Enum(UserStatus),
        nullable=False,
        default=UserStatus.pending,
    )
    email = sqlalchemy.Column(
        sqlalchemy.String(50),
        nullable=False,
        unique=True,
    )
    password_hash = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    external_id = sqlalchemy.Column(sqlalchemy.BigInteger, nullable=True)
