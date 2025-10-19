import typing
import pydantic


class ResumeId(pydantic.BaseModel):
    id: int


class ResumeCreateInfo(pydantic.BaseModel):
    name: str
    phone: str
    resume_link: str
    email: str
    confidencial: bool
    mallings: bool
    sms_ad: bool
    external_id: str | None


class ResumeInfo(ResumeId, ResumeCreateInfo):
    status: str


class ResumeUpdate(ResumeInfo):
    pass


class ResumeList(pydantic.BaseModel):
    resumes: typing.List[ResumeInfo]


class ResumeListResponse(pydantic.BaseModel):
    status: str
    details: str | None
    resumes: ResumeList | None


class ResumeInfoResponse(pydantic.BaseModel):
    status: str
    details: str | None
    resume: ResumeInfo
