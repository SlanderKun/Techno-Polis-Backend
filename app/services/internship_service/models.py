import sqlalchemy
import sqlalchemy.orm

import database.models
import services.resume_service.models


class Internship(database.models.Base):
    user_id: sqlalchemy.orm.Mapped[int] = (
        sqlalchemy.orm.mapped_column(sqlalchemy.ForeignKey("User.id"))
    )
    name = sqlalchemy.Column(sqlalchemy.String(1500))
    logo = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    company_name = sqlalchemy.Column(sqlalchemy.String(1500))
    platform = sqlalchemy.Column(
        sqlalchemy.Enum(services.resume_service.models.EnumPlatform),
        nullable=False,
        default=services.resume_service.models.EnumPlatform.alabushevo,
    )
    speciality = sqlalchemy.Column(
        sqlalchemy.Enum(services.resume_service.models.EnumSpeciality),
        nullable=False,
        default=services.resume_service.models.EnumSpeciality.hr,
    )
    responsibilities = sqlalchemy.Column(sqlalchemy.String(1500))
    requirements = sqlalchemy.Column(sqlalchemy.String(1500))
    official_employment = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    work_shedule = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    work_place = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    map_place = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    probation = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    salary = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    extra = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    text_promo = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    web_link = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    promo_link = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    confidencial = sqlalchemy.Column(sqlalchemy.Boolean)
    mailings = sqlalchemy.Column(sqlalchemy.Boolean)
    sms_ad = sqlalchemy.Column(sqlalchemy.Boolean)
