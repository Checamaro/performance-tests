from pathlib import Path

from seeds.schema.result import SeedsResult
import os
from tools.logger import get_logger

logger = get_logger("SEEDS_DUMPS")


def get_seeds_file_path(scenario: str) -> Path:
    """
    Возвращает путь к файлу с результатами сидинга для указанного сценария.

    :param scenario: Название сценария нагрузки
    :return: Полный путь к файлу
    """
    return Path(f"./dumps/{scenario}_seeds.json")

def save_seeds_results(result: SeedsResult, scenario: str):
    """
    Сохраняет результат сидинга (SeedsResult) в JSON-файл.

    :param result: Результат сидинга, сгенерированный билдером.
    :param scenario: Название сценария нагрузки, для которого создаются данные.
                     Используется для генерации имени файла (например, "credit_card_test").
    """
    seeds_file = get_seeds_file_path(scenario)

    if not os.path.exists("dumps"):
        os.mkdir("dumps")

    with open(f"./dumps/{scenario}_seeds.json", "w+", encoding="utf-8") as file:
        file.write(result.model_dump_json())

    logger.debug(f"Seeding result saved to file: {seeds_file}")

def load_seeds_results(scenario: str) -> SeedsResult:
    """
    Загружает результат сидинга из JSON-файла.

    :param scenario: Название сценария нагрузки, данные которого нужно загрузить.
    :return: Объект SeedsResult, восстановленный из файла.
    """
    seeds_file = get_seeds_file_path(scenario)

    logger.debug(f"Seeding result loaded from file: {seeds_file}")

    with open(f"./dumps/{scenario}_seeds.json", "r", encoding="utf-8") as file:
        return SeedsResult.model_validate_json(file.read())

