import uuid
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Модель данных пользователя
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True
    )

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserRequestSchema(BaseModel):
    """
    Модель запроса на создание пользователя
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """
    Модель ответа при успешном создании пользователя
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    user: UserSchema
