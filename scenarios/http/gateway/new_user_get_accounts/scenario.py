from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.schema import OpenDepositAccountResponseSchema
from clients.http.gateway.locust import GatewayHTTPSequentialTaskSet
from locust import task

from tools.locust.user import LocustBaseUser


class GetAccountsSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    """
    Нагрузочный сценарий, который последовательно:
    1. Создаёт нового пользователя.
    2. Открывает депозитный счёт.
    3. Получает списка счетов пользователя.

    Использует базовый GatewayHTTPSequentialTaskSet и уже созданных в нём API клиентов.
    """
    create_user_response: CreateUserResponseSchema | None = None
    open_deposit_account_response: OpenDepositAccountResponseSchema | None = None

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        """
        Открываем депозитный счёт для созданного пользователя.
        Проверяем, что предыдущий шаг был успешным.
        """
        if not self.create_user_response:
            return
        self.open_deposit_account_response = self.accounts_gateway_client.open_deposit_account(
            user_id=self.create_user_response.user.id
        )

    @task(6)
    def get_accounts(self):
        """
        Получаем список счетов, если счёт был успешно открыт.
        """
        if not self.open_deposit_account_response:
            return
        self.accounts_gateway_client.get_accounts(
            user_id=self.create_user_response.user.id
        )


class GetDocumentsUser(LocustBaseUser):
    """
    Пользователь Locust, исполняющий последовательный сценарий получения списка счетов.
    """
    tasks = [GetAccountsSequentialTaskSet]
