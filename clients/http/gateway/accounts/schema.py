from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum

from clients.http.gateway.cards.schema import CardSchema


class AccountType(StrEnum):
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"

class AccountStatus(StrEnum):
    ACTIVE = "ACTIVE"
    PENDING_CLOSURE = "PENDING_CLOSURE"
    CLOSED = "CLOSED"

class AccountSchema(BaseModel):
    """Описание структуры аккаунта"""
    id: str
    type: AccountType
    cards: list[CardSchema]
    status: AccountStatus
    balance: float


class GetAccountsQuerySchema(BaseModel):
    """
    Структура данных для получения списка счетов пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class GetAccountsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка счетов пользователя.
    """
    accounts: list[AccountSchema]


class OpenDepositAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия депозитного счета.
    """
    model_config = ConfigDict(populate_by_name=True)


    user_id: str = Field(alias="userId")


class OpenDepositAccountResponseSchema(BaseModel):
    """
    Описание структуры ответа для открытия депозитного счета.
    """
    account: AccountSchema


class OpenSavingsAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия сберегательного счета.
    """
    model_config = ConfigDict(populate_by_name=True)


    user_id: str = Field(alias="userId")


class OpenSavingsAccountResponseSchema(BaseModel):
    """
    Описание структуры ответа для открытия сберегательного счета.
    """
    account: AccountSchema


class OpenDebitCardAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия дебетового счета.
    """
    model_config = ConfigDict(populate_by_name=True)


    user_id: str = Field(alias="userId")


class OpenDebitCardAccountResponseSchema(BaseModel):
    """
    Описание структуры ответа для открытия дебетового счета.
    """
    account: AccountSchema

class OpenCreditCardAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия кредитного счета.
    """
    model_config = ConfigDict(populate_by_name=True)


    user_id: str = Field(alias="userId")


class OpenCreditCardAccountResponseSchema(BaseModel):
    """
    Описание структуры ответа для открытия кредитного счета.
    """
    account: AccountSchema