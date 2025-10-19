import enum
import sqlalchemy
import sqlalchemy.orm

import database.models


class ResumeStatus(enum.Enum):
    pending = "pending"
    rejected = "rejected"
    closed = "closed"
    opened = "opened"
    approved = "approved"


class Resume(database.models.Base):
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
