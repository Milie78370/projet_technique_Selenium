from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.Langue import Langue
from dotenv import load_dotenv
import os

load_dotenv()

@given("J'accede à la page dilitrust")
def accesPageOnboarding(context):
    context.driver.get(os.getenv('URL_SITE'))

@when('Je clique sur le bouton langue')
def jeCliqueButtonLang(context):
    Langue.clickBtnLang(context)

@when('Je choisis la "{langue}"')
def jeChoisisLang(context,langue):
    Langue.clickOtherLang(context, langue)

@Then('Je suis redirigé vers la page de la "{prefix_lang}"')
def redirectionPageLang(context, prefix_lang):
    get_new_url = context.driver.current_url
    url = f"https://auth.dilitrust.com/{prefix_lang}/"
    context.driver.implicitly_wait(5)
    assert url == get_new_url

