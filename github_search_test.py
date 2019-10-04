import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class GithubSearchTest(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.driver = webdriver.Remote(command_executor='http://18.232.75.227:8080:4444',desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})        
        self.base_url = "https://github.com"


    def test_github_repo_search_without_criteria(self):
        driver = self.driver
        driver.get(self.base_url)
        search_box = driver.find_element_by_name("q")
        search_box.send_keys(Keys.RETURN)
        assert "Search more than" in driver.page_source


    def test_github_repo_search_for_selenium(self):
        driver = self.driver
        driver.get(self.base_url)
        search_box = driver.find_element_by_name("q")
        search_box.send_keys("selenium")
        search_box.send_keys(Keys.RETURN)
        assert "We've found" in driver.page_source


    def test_github_repo_search_with_invalid_string(self):
        driver = self.driver
        driver.get(self.base_url)
        search_box = driver.find_element_by_name("q")
        search_box.send_keys("?*#^^%")
        search_box.send_keys(Keys.RETURN)
        assert "Your query contains a character that is ignored"  in driver.page_source


    def tearDown(self):
        self.driver.close()
