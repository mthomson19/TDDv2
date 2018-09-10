from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She kits Enter on the empty input box
        self.fail('write me!')
