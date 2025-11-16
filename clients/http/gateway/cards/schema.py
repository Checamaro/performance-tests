from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum


class CardType(StrEnum):
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"

class CardStatus(StrEnum):
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"

class CardPaymentSystem(StrEnum):
    MASTERCARD = "MASTERCARD"
    VISA = "VISA"

class CardSchema(BaseModel):
    """
    Описание структуры карты
    """
    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str = Field(alias="accountId")
    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: str = Field(alias="expiryDate")
    payment_system: CardPaymentSystem = Field(alias="paymentSystem")


class IssueVirtualCardRequestSchema(BaseModel):
    """
    Структура данных для создания новой виртуальной карты.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")


class IssueVirtualCardResponseSchema(BaseModel):
    """
    Описание структуры ответа для выпуска виртуальной карты.
    """
    card: CardSchema


class IssuePhysicalCardRequestSchema(BaseModel):
    """
    Структура данных для создания новой физической карты.
    """
    model_config = ConfigDict(populate_by_name=True)


    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")


class IssuePhysicalCardResponseSchema(BaseModel):
    """
    Описание структуры ответа для выпуска физической карты.
    """
    card: CardSchema