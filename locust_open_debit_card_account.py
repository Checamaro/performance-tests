from locust import task, User, between
from clients.http.gateway.users.client import build_users_gateway_locust_http_client, UsersGatewayHTTPClient
from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserResponseSchema


class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)
    users_gateway_client: UsersGatewayHTTPClient
    create_user_response: CreateUserResponseSchema
    accounts_gateway_client: AccountsGatewayHTTPClient

    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        self.accounts_gateway_client.open_debit_card_account(self.create_user_response.user.id)