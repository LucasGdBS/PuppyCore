from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def set_up():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--icognito') 
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        
        
        return driver

class TesteTutor(TestCase):

    def teste_cadastrar(self):
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')
        sleep(2)

        
        driver.find_element(By.ID, 'cadastrar_tutor').click()
        
        driver.find_element(By.ID, 'nome').send_keys('Homem de Ferro')
        driver.find_element(By.ID, 'cpf').send_keys('123.864.286-88')
        driver.find_element(By.ID, 'dataNascimento').send_keys('01071960')
        driver.find_element(By.ID, 'celular').send_keys('(81)946271597')
        driver.find_element(By.ID, 'email').send_keys('ironman@vingadores.com')
        sleep(1)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(1)        
        driver.close()
    
    def teste_cadastro_cpf_repetido(self):
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')
        sleep(2)

        for i in range(2):
            driver.find_element(By.ID, 'cadastrar_tutor').click()
            
            driver.find_element(By.ID, 'nome').send_keys('Tanos')
            driver.find_element(By.ID, 'cpf').send_keys('159.753.147-66')
            driver.find_element(By.ID, 'dataNascimento').send_keys('01021973')
            driver.find_element(By.ID, 'celular').send_keys('(81)915975324')
            driver.find_element(By.ID, 'email').send_keys('thanos@joiadoinfinito.com')
            sleep(1)
            driver.find_element(By.ID, 'enviar').click()
            sleep(1)
            driver.find_element(By.ID, 'confirmar').click()
            sleep(1)
        driver.find_element(By.ID, "cancelar").click()
        sleep(1)        
        driver.close()
    
    def teste_cadastro_dado_faltando(self):
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')

        driver.find_element(By.ID, 'cadastrar_tutor').click()
        driver.find_element(By.ID, 'nome').send_keys('Visão')
        driver.find_element(By.ID, 'cpf').send_keys('178.654.258.44')
        driver.find_element(By.ID, 'dataNascimento').send_keys('01101968')
        driver.find_element(By.ID, 'celular').send_keys('(81)915975324')
        driver.find_element(By.ID, 'enviar').click()
        
        driver.close()

    def teste_cadastro_email_incorreto(self): # Pode estar incorreto
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')

        driver.find_element(By.ID, 'cadastrar_tutor').click()
        driver.find_element(By.ID, 'nome').send_keys('Visão')
        driver.find_element(By.ID, 'cpf').send_keys('178.654.258.44')
        driver.find_element(By.ID, 'dataNascimento').send_keys('01101968')
        driver.find_element(By.ID, 'celular').send_keys('(81)915975324')
        driver.find_element(By.ID, 'email').send_keys('visao@joiadamente')
        driver.find_element(By.ID, 'enviar').click()
        sleep(3)

        driver.find_element(By.ID, 'enviar').click()

        driver.close()
    

    def teste_add_pets(self):
        pass
    
    def teste_add_faltando_dado(self):
        pass

    def teste_add_vacina(self):
        pass

    def teste_add_faltando_dado(self):
        pass

    def teste_ver_vacinas(self):
        pass
    
    def teste_ver_tutores(self):
        pass

    def teste_ver_info_tutor(self):
        pass

    def teste_dados_alterar_preenchidos(self):
        pass
    
    def teste_alterar_cadastro(self):
        pass
    
    def teste_alterar_cadastro_faltando_dados(self):
        pass

    def teste_ver_pets(self):
        pass

    def teste_ver_info_pet(self):
        pass

    def teste_abrir_vacina(self):
        pass

    def teste_conferir_vacina_pet(self):
        pass

    


    

        
             



        