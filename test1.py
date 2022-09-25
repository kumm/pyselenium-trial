# Implementation of Selenium WebDriver with Python using PyTest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


def test_lambdatest_todo_app():
    ff_driver = webdriver.Firefox()
    ff_driver.get('https://lambdatest.github.io/sample-todo-app/')
    ff_driver.maximize_window()
    ff_driver.find_element(By.NAME,"li1").click()
    ff_driver.find_element(By.NAME,"li2").click()
    title = "Sample page - lambdatest.com"
    assert title == ff_driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field = ff_driver.find_element(By.ID, "sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(1)
    lis = ff_driver.find_elements(By.XPATH,"//ul/li")
    ff_driver.find_element(By.XPATH,"//input[@value='add' and @type='submit']").click()
    el = findNthSpan(ff_driver, len(lis) + 1)
    assert el.text == sample_text

    sleep(2)
    ff_driver.quit()


def findNthSpan(ff_driver, ndx):
    return WebDriverWait(ff_driver, 3000).until(
        lambda driver: ff_driver.find_element(By.XPATH, f"//input[@name='li{ndx}']/following-sibling::span"))


if __name__ == '__main__':
    test_lambdatest_todo_app()
