import sqlalchemy

import database.models


class Session(database.models.BaseTable):
    __tablename__ = 'sessions'

    user_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('users.pk'),
        primary_key=True,
    )
    key = sqlalchemy.Column(
        sqlalchemy.String(255),
        nullable=False,
        unique=True,
    )
    location = sqlalchemy.Column(sqlalchemy.String(255), nullable=True)
