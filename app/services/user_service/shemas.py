import pydantic


class UserInfoSchema(pydantic.BaseModel):
    email: str
    status: str
    representative_name: str | None
    representative_surname: str | None
    company_name: str | None
    logo: str | None
    inn: str | None
    contact_number: str | None
    contact_email: str | None


class UserInfoResponse(pydantic.BaseModel):
    status: str
    details: str | None
    data: UserInfoSchema | None
