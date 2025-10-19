import typing

import database.models
import sqlalchemy
import sqlalchemy.orm


class UniversityInfo(database.models.Base):
    __tablename__ = "universities_info"

    id: sqlalchemy.orm.Mapped[database.models.intpk]
    created_at: sqlalchemy.orm.Mapped[database.models.created_at]
    updated_at: sqlalchemy.orm.Mapped[database.models.updated_at]

    representative_name: sqlalchemy.orm.Mapped[str]
    representative_surname: sqlalchemy.orm.Mapped[str]
    company_name: sqlalchemy.orm.Mapped[str]
    logo: sqlalchemy.orm.Mapped[typing.Annotated[str, None]]
    inn: sqlalchemy.orm.Mapped[str]
    contact_number: sqlalchemy.orm.Mapped[str]
    contact_email: sqlalchemy.orm.Mapped[str]
