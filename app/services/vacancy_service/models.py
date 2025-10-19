import enum
import sqlalchemy
import sqlalchemy.orm

import database.models


class EnumPlatform(enum.Enum):
    alabushevo = "alabushevo"
    pechatniki = "pechatniki"
    rudnevo = "rudnevo"
    micron = "micron"
    angstrem = "angstrem"
    miet = "miet"


class EnumSpeciality(enum.Enum):
    hr = "hr"
    it = "it"
    administrative_job = "administrative_job"
    logistic = "logistic"
    marketing = "marketing"
    medecine = "medecine"
    microelectronic = "microelectronic"
    sales = "sales"
    production = "production"
    finance = "finance"
    law = "law"


class Vacancy(database.models.Base):
    user_id = sqlalchemy.orm.mapped_column(sqlalchemy.ForeignKey("User.id"))
    name = sqlalchemy.Column(sqlalchemy.String(1500))
    logo = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)
    company_name = sqlalchemy.Column(sqlalchemy.String(1500))
    platform = sqlalchemy.Column(
        sqlalchemy.Enum(EnumPlatform),
        nullable=False,
        default=EnumPlatform.alabushevo,
    )
    speciality = sqlalchemy.Column(
        sqlalchemy.Enum(EnumSpeciality),
        nullable=False,
        default=EnumSpeciality.hr,
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
