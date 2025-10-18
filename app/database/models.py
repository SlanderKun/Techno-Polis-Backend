import datetime
import typing

import sqlalchemy
import sqlalchemy.orm

intpk = typing.Annotated[int, sqlalchemy.orm.mapped_column(primary_key=True)]
created_at = typing.Annotated[
    datetime.datetime,
    sqlalchemy.orm.mapped_column(
        server_default=sqlalchemy.text("TIMEZONE('utc', now())")
    ),
]
updated_at = typing.Annotated[
    datetime.datetime,
    sqlalchemy.orm.mapped_column(
        server_default=sqlalchemy.text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    ),
]


class Base(sqlalchemy.orm.DeclarativeBase):
    pass


class BaseTable(Base):
    __abstract__ = True

    id: sqlalchemy.orm.Mapped[intpk]
    created_at: sqlalchemy.orm.Mapped[created_at]
    updated_at: sqlalchemy.orm.Mapped[updated_at]
