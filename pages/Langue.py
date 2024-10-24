import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Classe Langue qui centralise la logique metier du test
class Langue:

    def clickBtnLang(context):
        element = context.driver.find_element(By.ID, "login-language-switcher-tab-button-dropdown")
        element.click()

    def clickOtherLang(context, langue):
        option_button = context.driver.find_element(By.ID, langue)
        option_button.click()