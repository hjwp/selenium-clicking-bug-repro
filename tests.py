import unittest
from selenium import webdriver
import subprocess

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element

class QuickTest(unittest.TestCase):
    def setUp(self):
        server = subprocess.Popen(
            ['python', '-m', 'http.server', '8101']
        )
        self.addCleanup(server.kill)
        self.driver = webdriver.Firefox()
        self.addCleanup(self.driver.quit)


    def test_clicking_around_fast(self):
        self.driver.get('http://localhost:8101')
        header_locator = (By.CSS_SELECTOR, 'h1')
        WebDriverWait(self.driver, 2).until(
            text_to_be_present_in_element(header_locator, 'Index page')
        )
        for _ in range(20):
            self.driver.find_element_by_link_text('page 2').click()
            WebDriverWait(self.driver, 2).until(
                text_to_be_present_in_element(header_locator, 'Page 2')
            )
            self.driver.find_element_by_link_text('page 3').click()
            WebDriverWait(self.driver, 2).until(
                text_to_be_present_in_element(header_locator, 'Page 3')
            )
            self.driver.find_element_by_link_text('index page').click()
            WebDriverWait(self.driver, 2).until(
                text_to_be_present_in_element(header_locator, 'Index page')
            )


if __name__ == '__main__':
    unittest.main()

