import typing
import sqlalchemy
import sqlalchemy.orm

import database.models


class User(database.models.Base):
    __tablename__ = "users"

    id: sqlalchemy.orm.Mapped[database.models.intpk]
    created_at: sqlalchemy.orm.Mapped[database.models.created_at]
    updated_at: sqlalchemy.orm.Mapped[database.models.updated_at]

    username: sqlalchemy.orm.Mapped[
        typing.Annotated[str, sqlalchemy.orm.mapped_column(unique=True)]
    ]
