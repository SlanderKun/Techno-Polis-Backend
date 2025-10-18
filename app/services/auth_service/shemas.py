import pydantic


class RegisterRequestSchema(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: str


class LoginRequestSchema(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: str
