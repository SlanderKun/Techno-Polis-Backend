import enum
import typing
import database.models
import sqlalchemy
import sqlalchemy.orm


class ResumeStatus(enum.Enum):
    pending = "pending"
    rejected = "rejected"
    closed = "closed"
    opened = "opened"
    approved = "approved"


class Resume(database.models.Base):
    __tablename__ = "resumes"

    id: sqlalchemy.orm.Mapped[database.models.intpk]
    created_at: sqlalchemy.orm.Mapped[database.models.created_at]
    updated_at: sqlalchemy.orm.Mapped[database.models.updated_at]

    status = sqlalchemy.Column(
        sqlalchemy.Enum(ResumeStatus),
        nullable=False,
        default=ResumeStatus.pending,
    )
    name = sqlalchemy.Column(sqlalchemy.String(1500))
    phone = sqlalchemy.Column(sqlalchemy.String(1500))
    resume_link = sqlalchemy.Column(sqlalchemy.String(1500))
    email = sqlalchemy.Column(sqlalchemy.String(1500))
    confidencial = sqlalchemy.Column(sqlalchemy.Boolean)
    mallings = sqlalchemy.Column(sqlalchemy.Boolean)
    sms_ad = sqlalchemy.Column(sqlalchemy.Boolean)
    external_id: sqlalchemy.orm.Mapped[typing.Annotated[int, None]]
