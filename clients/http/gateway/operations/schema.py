from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from enum import StrEnum
from datetime import datetime
from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"


class OperationReceiptSchema(BaseModel):
    url: HttpUrl
    document: str


class BaseOperationSchema(BaseModel):
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationsSummarySchema(BaseModel):
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationsResponseSchema(BaseModel):
    operations: list[BaseOperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    summary: OperationsSummarySchema


class GetOperationReceiptResponseSchema(BaseModel):
    receipt: OperationReceiptSchema


class GetOperationResponseSchema(BaseModel):
    operation: BaseOperationSchema


class MakeFeeOperationResponseSchema(BaseModel):
    operation: BaseOperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    operation: BaseOperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    operation: BaseOperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    operation: BaseOperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    operation: BaseOperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    operation: BaseOperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    operation: BaseOperationSchema


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class BaseOperationRequestSchema(BaseModel):
    """
    Базовая структура данных для создания операций.
    Содержит общие поля для всех типов операций.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(BaseOperationRequestSchema):
    """
    Структура данных для создания операции комиссии.
    Наследует все поля из BaseOperationRequestSchema.
    """


class MakeTopUpOperationRequestSchema(BaseOperationRequestSchema):
    """
    Структура данных для создания операции пополнения.
    Наследует все поля из BaseOperationRequestSchema.
    """


class MakeCashbackOperationRequestSchema(BaseOperationRequestSchema):
    """
    Структура данных для создания операции кэшбэка.
    Наследует все поля из BaseOperationRequestSchema.
    """


class MakeTransferOperationRequestSchema(BaseOperationRequestSchema):
    """
    Структура данных для создания операции перевода.
    Наследует все поля из BaseOperationRequestSchema.
    """


class MakePurchaseOperationRequestSchema(BaseOperationRequestSchema):
    """
    Структура данных для создания операции покупки.
    Наследует базовые поля и добавляет категорию покупки.
    """
    category: str = Field(default_factory=fake.category)


class MakeBillPaymentOperationRequestSchema(BaseOperationRequestSchema):
    """
    Структура данных для создания операции оплаты по счету.
    Наследует все поля из BaseOperationRequestSchema.
    """


class MakeCashWithdrawalOperationRequestSchema(BaseOperationRequestSchema):
    """
    Структура данных для создания операции снятия наличных денег.
    Наследует все поля из BaseOperationRequestSchema.
    """
