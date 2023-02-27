import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestAddAnimeForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/")

    def tearDown(self):
        self.driver.close()

    def test_add_anime_form(self):
        title_input = self.driver.find_element('title')
        title_input.send_keys('My Anime Title')

        genre_input = self.driver.find_element('genre')
        genre_input.send_keys('My Anime Genre')

        description_input = self.driver.find_element('description')
        description_input.send_keys('My Anime Description')

        type_input = self.driver.find_element('type')
        type_input.send_keys('My Anime Type')

        producer_input = self.driver.find_element('producer')
        producer_input.send_keys('My Anime Producer')

        studio_input = self.driver.find_element('studio')
        studio_input.send_keys('My Anime Studio')

        submit_button = self.driver.find_element_by_xpath('//button[@type="submit"]')
        submit_button.click()

        # Attendre que la réponse du backend soit reçue
        result_div = self.driver.find_element_by_class_name('result')
        prediction_text = result_div.text

        # Vérifiez que la prédiction est un nombre compris entre 0 et 10
        prediction = float(prediction_text)
        self.assertGreaterEqual(prediction, 0)
        self.assertLessEqual(prediction, 10)

if __name__ == '__main__':
    unittest.main()
