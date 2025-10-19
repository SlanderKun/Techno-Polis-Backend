import pydantic


class UniversityCreateSchema(pydantic.BaseModel):
    representative_name: str
    representative_surname: str
    company_name: str
    logo: str | None = None
    inn: str
    contact_number: str
    contact_email: str

    class Config:
        orm_mode = True


class UniversityUpdateSchema(UniversityCreateSchema):
    id: int
