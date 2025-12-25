from pydantic_settings import BaseSettings, SettingsConfigDict

import locust.stats

from tools.config.grpc import GRPCClientConfig
from tools.config.http import HTTPClientConfig
from tools.config.locust import LocustUserConfig

locust.stats.PERCENTILES_TO_REPORT = [0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99, 1.0]
locust.stats.CSV_STATS_INTERVAL_SEC = 5
locust.stats.HISTORY_STATS_INTERVAL_SEC = 5
locust.stats.CONSOLE_STATS_INTERVAL_SEC =5
locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 5

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )

    locust_user: LocustUserConfig
    gateway_http_client: HTTPClientConfig
    gateway_grpc_client: GRPCClientConfig

settings = Settings()