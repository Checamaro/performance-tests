from clients.http.client import HTTPClient
from typing import TypedDict
from httpx import Response


class CreateCardsRequestDict(TypedDict):
    """
    Структура данных для создания новой виртуальной/физической карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):

    def issue_virtual_card_api(self, request: CreateCardsRequestDict) -> Response:
        """
        Создание новой виртуальной карты.

        :param request: Словарь с данными новой виртуальной карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreateCardsRequestDict) -> Response:
        """
        Создание новой физической карты.

        :param request: Словарь с данными новой физической карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
