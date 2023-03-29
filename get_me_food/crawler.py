import requests
import bs4
from urllib.parse import urljoin


class Crawler:

    RECIPE_URL = "https://prohomecooks.com/blogs/recipes/theres-no-such-thing-as-too-many-banana-recipes"
    BASE_URL = "https://prohomecooks.com/blogs/recipes"

    def __init__(self, url: str) -> None:
        html_page = requests.get(url, timeout=3).text
        self.__soup = bs4.BeautifulSoup(html_page, 'html.parser')

    def __get_recipe_elements(self) -> str:
        recipe = []
        for list_element in self.__soup.find_all("li"):
            recipe.append(list_element.get_text())
        return recipe

    def __find_recipe(self, ingredient: str) -> str:
        recipe = self.__get_recipe_elements()
        return any(ingredient.lower() in recipe_step.lower() for recipe_step in recipe)

    def extract_all_recipes(self) -> list[str]:
        """Extract all recipes from the base link.

        The recipe links are considered to have the keyword "recipe" in the URL.

        Returns:
            list[str]: URLs to all found recipes form the base URL.
        """
        main_url = "https://prohomecooks.com"
        recipes = [urljoin(main_url, recipe.get("href"))
                   for recipe in self.__soup.find_all('a') if "recipe" in recipe.get("href")]
        return recipes


test_crawler = Crawler(Crawler.BASE_URL)
recipes = test_crawler.extract_all_recipes()
print(recipes)
