import sqlalchemy
import sqlalchemy.orm

import database.models


class Session(database.models.Base):
    __tablename__ = "sessions"

    id: sqlalchemy.orm.Mapped[database.models.intpk]
    created_at: sqlalchemy.orm.Mapped[database.models.created_at]
    updated_at: sqlalchemy.orm.Mapped[database.models.updated_at]

    user_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("users.id"),
        primary_key=True,
    )
    key = sqlalchemy.Column(
        sqlalchemy.String(255),
        nullable=False,
        unique=True,
    )
    location = sqlalchemy.Column(sqlalchemy.String(255), nullable=True)
