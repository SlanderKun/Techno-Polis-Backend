import enum
import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey

import database.models
from sqlalchemy.orm import Mapped


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
    password_hash = sqlalchemy.Column(sqlalchemy.String(1500), nullable=False)
    external_id = sqlalchemy.Column(sqlalchemy.BigInteger, nullable=True)

class Session(database.models.Base):
    __tablename__ = "sessions"

    user_id : Mapped[int] = mapped_column(ForeignKey("User.id")) #Первичный ключ + связка с таблицей user хз как делать
    location = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True)

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
        default=UserStatus.pending,
    )
    name = sqlalchemy.Column(sqlalchemy.String(1500))
    phone = sqlalchemy.Column(sqlalchemy.String(1500))
    resume_link = sqlalchemy.Column(sqlalchemy.String(1500))
    email = sqlalchemy.Column(sqlalchemy.String(1500))
    confidencial = sqlalchemy.Column(sqlalchemy.Boolean)
    mallings = sqlalchemy.Column(sqlalchemy.Boolean)
    sms_ad = sqlalchemy.Column(sqlalchemy.Boolean)

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
    user_id : Mapped[int] = mapped_column(ForeignKey("User.id"))
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
    responsibilities = sqlalchemy.Column(sqlalchemy.String(1500)) #Надо уточнить тип
    requirements = sqlalchemy.Column(sqlalchemy.String(1500)) #Надо уточнить тип
    official_employment = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True) #Ограничение по символам уточнить
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

class Internship(database.models.Base):
    user_id : Mapped[int] = mapped_column(ForeignKey("User.id"))
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
    responsibilities = sqlalchemy.Column(sqlalchemy.String(1500)) #Надо уточнить тип
    requirements = sqlalchemy.Column(sqlalchemy.String(1500)) #Надо уточнить тип
    official_employment = sqlalchemy.Column(sqlalchemy.String(1500), nullable=True) #Ограничение по символам уточнить
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
