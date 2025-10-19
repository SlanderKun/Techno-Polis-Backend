import typing

import pydantic


class VacancyData(pydantic.BaseModel):
    owner: int
    name: str
    logo: str | None
    company_name: str
    platform: str
    speciality: str
    responsibilities: str
    requirements: str
    official_employment: str | None
    work_shedule: str | None
    work_place: str | None
    map_place: str | None
    probation: str | None
    salary: str | None
    extra: str | None
    text_promo: str | None
    web_link: str | None
    promo_link: str | None
    confidencial: bool
    mailings: bool
    sms_ad: bool


class VacancyListResponse(pydantic.BaseModel):
    status: str
    details: str | None
    internships: typing.List[VacancyData]
