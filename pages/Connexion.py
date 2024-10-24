import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Classe Connexion qui centralise la logique metier du test
class Connexion:

    def enterEmail(context, email):
        element = context.driver.find_element(By.ID, "login-name-input")
        element.clear()
        element.send_keys(email)

    def enterPassword(context, password):
        element = context.driver.find_element(By.ID, "login-password-input")
        element.clear()
        element.send_keys(password)

    def clickBtn(context):
        element = context.driver.find_element(By.ID, "login-button")
        element.click()

    def elementDisplayed(context, result):
        context.driver.implicitly_wait(5)
        if result == "Invalid mail":
            invalid_email = context.driver.find_element(By.ID, "login-form-error-0")
            assert invalid_email.is_displayed()
        else:
            password_element = context.driver.find_element(By.ID, "login-password")
            assert password_element.is_displayed()


