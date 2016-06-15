import unittest
from selenium import webdriver
import subprocess

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class QuickTest(unittest.TestCase):
    def setUp(self):
        server = subprocess.Popen(
            ['python', '-m', 'http.server', '8101']
        )
        self.addCleanup(server.kill)
        # capabilities = DesiredCapabilities.FIREFOX
        # capabilities['marionette'] = True
        # capabilities['binary'] = '/home/harry/Downloads/firefox46/firefox'
        self.driver = webdriver.Firefox(
            firefox_binary=FirefoxBinary('/home/harry/Downloads/firefox46/firefox')
        )
        self.addCleanup(self.driver.quit)
        self.driver.implicitly_wait(1)


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

