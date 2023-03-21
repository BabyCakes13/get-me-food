"""Module which implements the command line arguments."""
import argparse


class CMDArguments(object):
    """Handles the command line arguments of the application."""

    HELP_VERBOSE = "increase verbosity"

    def __init__(self, argv) -> None:
        self.__arguments = []

        self.__setup_parser(argv)

    def ingredients(self) -> list[str]:
        return self.__arguments.ingredients

    def __setup_parser(self, argv: list) -> None:
        parser = argparse.ArgumentParser()

        parser.add_argument("-v", "--verbose", action="store_true", help="increase verbosity")
        parser.add_argument("--ingredients", dest="ingredients", nargs='+',
                            required=True, help="list of ingredients")
        self.__arguments = parser.parse_args(argv)
