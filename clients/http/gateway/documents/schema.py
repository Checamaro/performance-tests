from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class DocumentSchema(BaseModel):
    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Структура данных для получения документа тарифа.
    """
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Структура данных для получения документа контракта.
    """
    contract: DocumentSchema
