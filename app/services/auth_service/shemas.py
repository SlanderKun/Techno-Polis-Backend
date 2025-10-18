import pydantic


class RegisterRequestSchema(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: str


class LoginRequestSchema(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: str


class ErrorResponse(pydantic.BaseModel):
    status: str
    detail: str


class RegisterResponse(pydantic.BaseModel):
    status: str
    detail: str
