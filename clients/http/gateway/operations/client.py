from clients.http.client import HTTPClient, HTTPClientExtensions
from httpx import Response, QueryParams
from locust.env import Environment

from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from clients.http.gateway.operations.schema import GetOperationsQuerySchema, GetOperationsSummaryQuerySchema, \
    GetOperationsResponseSchema, GetOperationsSummaryResponseSchema, GetOperationReceiptResponseSchema, \
    GetOperationResponseSchema, MakeFeeOperationResponseSchema, MakeFeeOperationRequestSchema, \
    MakeTopUpOperationRequestSchema, MakeCashbackOperationRequestSchema, MakeTransferOperationRequestSchema, \
    MakePurchaseOperationRequestSchema, MakeBillPaymentOperationRequestSchema, MakeTopUpOperationResponseSchema, \
    MakeCashWithdrawalOperationRequestSchema, MakeCashbackOperationResponseSchema, MakeTransferOperationResponseSchema, \
    MakePurchaseOperationResponseSchema, MakeBillPaymentOperationResponseSchema, \
    MakeCashWithdrawalOperationResponseSchema

from tools.routes import APIRoutes


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
        return self.get(
            f"{APIRoutes.OPERATIONS}/{operation_id}",
            extensions=HTTPClientExtensions(route=f"{APIRoutes.OPERATIONS}/{{operation_id}}")
        )

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции.

        :param operation_id: UUID идентификатор операции
        :return: Ответ сервера с данными чека
        """
        return self.get(
            f"{APIRoutes.OPERATIONS}/operation-receipt/{operation_id}",
            extensions=HTTPClientExtensions(route=f"{APIRoutes.OPERATIONS}/operation-receipt/{{operation_id}}")
        )

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получение списка операций для определенного счета.

        :param query: Параметры запроса с идентификатором счета
        :return: Ответ сервера со списком операций
        """
        return self.get(
            APIRoutes.OPERATIONS,
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route=APIRoutes.OPERATIONS)
        )

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param query: Параметры запроса с идентификатором счета
        :return: Ответ сервера со статистикой операций
        """
        return self.get(
            f"{APIRoutes.OPERATIONS}/operations-summary",
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route=f"{APIRoutes.OPERATIONS}/operations-summary")
        )

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Создание операции комиссии.

        :param request: Данные для создания операции комиссии
        :return: Ответ сервера с результатом создания операции
        """
        return self.post(f"{APIRoutes.OPERATIONS}/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Создание операции пополнения счета.

        :param request: Данные для создания операции пополнения
        :return: Ответ сервера с результатом создания операции
        """
        return self.post(f"{APIRoutes.OPERATIONS}/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Создание операции кэшбэка.

        :param request: Данные для создания операции кэшбэка
        :return: Ответ сервера с результатом создания операции
        """
        return self.post(f"{APIRoutes.OPERATIONS}/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Создание операции перевода средств.

        :param request: Данные для создания операции перевода
        :return: Ответ сервера с результатом создания операции
        """
        return self.post(f"{APIRoutes.OPERATIONS}/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Создание операции покупки.

        :param request: Данные для создания операции покупки, включая категорию
        :return: Ответ сервера с результатом создания операции
        """
        return self.post(f"{APIRoutes.OPERATIONS}/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Создание операции оплаты по счету.

        :param request: Данные для создания операции оплаты счета
        :return: Ответ сервера с результатом создания операции
        """
        return self.post(f"{APIRoutes.OPERATIONS}/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Создание операции снятия наличных денег.

        :param request: Данные для создания операции снятия наличных
        :return: Ответ сервера с результатом создания операции
        """
        return self.post(f"{APIRoutes.OPERATIONS}/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str,
                                       account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())


def build_operations_gateway_locust_http_client(environment: Environment) -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр OperationsGatewayHTTPClient с хуками сбора метрик.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))
