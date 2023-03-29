class Providers(object):

    def __init__(self, providers: list[str]) -> None:
        self.__providers = providers

    def providers(self) -> list[str]:
        return self.__providers

    def __str__(self) -> str:
        return "Providers[{}]".format(self.__providers)
