from grpc import Channel, insecure_channel


def build_gateway_grpc_client() -> Channel:
    """
    Фабричная функция (билдер) для создания grpc-канала к сервису grpc-gateway.
    :return: gRPC-канал (Channel), настроенный на localhost: 9003.
    """
    return insecure_channel("localhost:9003")
