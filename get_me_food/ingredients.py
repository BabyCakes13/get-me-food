class Ingredients(object):

    def __init__(self, ingredients: list[str]) -> None:
        self.__ingredients = ingredients

    def ingredients(self) -> list[str]:
        return self.__ingredients

    def __str__(self) -> str:
        return "Ingredients[{}]".format(self.__ingredients)
