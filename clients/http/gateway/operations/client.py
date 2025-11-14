from clients.http.client import HTTPClient
from typing import TypedDict
from httpx import Response, QueryParams

from clients.http.gateway.client import build_gateway_http_client


class OperationReceiptDict(TypedDict):
    url: str
    document: str


class BaseOperationDict(TypedDict):
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationsSummaryDict(TypedDict):
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsResponseDict(TypedDict):
    operations: list[BaseOperationDict]


class GetOperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummaryDict


class GetOperationReceiptResponseDict(TypedDict):
    receipt: OperationReceiptDict


class GetOperationResponseDict(TypedDict):
    operation: BaseOperationDict


class MakeFeeOperationResponseDict(TypedDict):
    operation: BaseOperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    operation: BaseOperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    operation: BaseOperationDict


class MakeTransferOperationResponseDict(TypedDict):
    operation: BaseOperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    operation: BaseOperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    operation: BaseOperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    operation: BaseOperationDict


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

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(cardId=card_id, accountId=account_id, status="COMPLETED", amount=1500.00)
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(cardId=card_id, accountId=account_id, status="COMPLETED", amount=55.77)
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(cardId=card_id, accountId=account_id, status="COMPLETED",
                                                   amount=55.77)
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(cardId=card_id, accountId=account_id, status="COMPLETED",
                                                   amount=55.77)
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(cardId=card_id, accountId=account_id, status="COMPLETED",
                                                   amount=55.77, category="restaurant")
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(cardId=card_id, accountId=account_id, status="COMPLETED",
                                                      amount=55.77)
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(cardId=card_id, accountId=account_id, status="COMPLETED",
                                                         amount=55.77)
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
