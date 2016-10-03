# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import os 
 
class NewVisitorTest(unittest.TestCase):
 
    def setUp(self):
        self.chromedriver = "/usr/bin/chromedriver"
        os.environ["webdriver.chrome.driver"] = self.chromedriver
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def test_it_worked(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Bul Shit', self.browser.title)
 
if __name__ == '__main__':
    unittest.main(warnings='ignore')
