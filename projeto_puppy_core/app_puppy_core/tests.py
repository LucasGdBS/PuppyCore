from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#Teste rapido 
class TesteTutor(TestCase):
    def teste(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--icognito') 
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('http://127.0.0.1:8000/')

        login = driver.find_element(By.ID, 'login')
        login.click()
        sleep(2)
        driver.quit()

