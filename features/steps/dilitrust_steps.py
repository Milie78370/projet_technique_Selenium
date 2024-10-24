from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.Connexion import Connexion
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os

load_dotenv()

@given("J'accede à la page onboarding de dilitrust")
def accesPageOnboarding(context):
    context.driver.get(os.getenv('URL_SITE'))

@when('Je saisie un "{email}" valide')
def jeSaisieEmail(context,email):
    Connexion.enterEmail(context, email)

@when('Je saisie un "{password}"')
def jeSaisiePassword(context,password):
    Connexion.enterPassword(context, password)

@when('Je clique sur le bouton validation')
def jeCliqueButton(context):
    Connexion.clickBtn(context)

@Then('Je vois "{result}"')
def MdpApparait(context, result):
    Connexion.elementDisplayed(context, result)

