"""Module which implements the logic of the application."""
import logging

from get_me_food.ingredients import Ingredients
from get_me_food.providers import Providers
console_logger = logging.getLogger('console')
info_logger = logging.getLogger('info_file')
error_logger = logging.getLogger('error_file')


class GetMeFood:
    """Entrypoint of the application."""

    def __init__(self, ingredients: list[str], providers: list[str]) -> None:
        console_logger.debug("Setup GetMeFood class.")
        self.__ingredients = Ingredients(ingredients)
        self.__providers = Providers(providers)

    def __str__(self) -> str:
        return f"GetMeFood[{self.__ingredients}, {self.__providers}]"
