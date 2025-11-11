from clients.http.client import HTTPClient
from typing import TypedDict
from httpx import Response, QueryParams


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    accountId: str


class BaseOperationRequestDict(TypedDict):
    """
    Базовая структура данных для создания операций.
    Содержит общие поля для всех типов операций.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции комиссии.
    Наследует все поля из BaseOperationRequestDict.
    """


class MakeTopUpOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции пополнения.
    Наследует все поля из BaseOperationRequestDict.
    """


class MakeCashbackOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции кэшбэка.
    Наследует все поля из BaseOperationRequestDict.
    """


class MakeTransferOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции перевода.
    Наследует все поля из BaseOperationRequestDict.
    """


class MakePurchaseOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    Наследует базовые поля и добавляет категорию покупки.
    """
    category: str


class MakeBillPaymentOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции оплаты по счету.
    Наследует все поля из BaseOperationRequestDict.
    """


class MakeCashWithdrawalOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных для создания операции снятия наличных денег.
    Наследует все поля из BaseOperationRequestDict.
    """


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с API операций (/api/v1/operations) сервиса http-gateway.

    Предоставляет методы для работы с операциями: получение информации, создание операций,
    получение чеков и статистики.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по её идентификатору.

        :param operation_id: UUID идентификатор операции
        :return: Ответ сервера с данными операции
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции.

        :param operation_id: UUID идентификатор операции
        :return: Ответ сервера с данными чека
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета.

        :param query: Параметры запроса с идентификатором счета
        :return: Ответ сервера со списком операций
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param query: Параметры запроса с идентификатором счета
        :return: Ответ сервера со статистикой операций
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.

        :param request: Данные для создания операции комиссии
        :return: Ответ сервера с результатом создания операции
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения счета.

        :param request: Данные для создания операции пополнения
        :return: Ответ сервера с результатом создания операции
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка.

        :param request: Данные для создания операции кэшбэка
        :return: Ответ сервера с результатом создания операции
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создание операции перевода средств.

        :param request: Данные для создания операции перевода
        :return: Ответ сервера с результатом создания операции
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.

        :param request: Данные для создания операции покупки, включая категорию
        :return: Ответ сервера с результатом создания операции
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету.

        :param request: Данные для создания операции оплаты счета
        :return: Ответ сервера с результатом создания операции
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных денег.

        :param request: Данные для создания операции снятия наличных
        :return: Ответ сервера с результатом создания операции
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)