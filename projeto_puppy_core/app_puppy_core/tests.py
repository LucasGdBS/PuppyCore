from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#Teste rapido 
class TesteTutor(TestCase):

    def teste_puppycore(self):
        # Abre o navegador e a pagina do PuppyCore
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--icognito') 
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/')

        # CLica no botão de efetuar login
        sleep(1)
        botao_entrada = driver.find_element(By.ID, 'login')
        botao_entrada.click()
        sleep(1)
        login = driver.find_element(By.ID, 'login')
        login.click()
        sleep(1)
        
        # Teste para cadastrar 2 vezes o mesmo CPF
        for i in range(2):
            cadastrar_tutor = driver.find_element(By.ID, 'cadastrar_tutor')
            cadastrar_tutor.click()
            nome = driver.find_element(By.ID, 'nome')
            nome.send_keys('Thanos')
            cpf = driver.find_element(By.ID, 'cpf')
            cpf.send_keys('159.753.147-66')
            data = driver.find_element(By.ID, 'dataNascimento')
            data.send_keys('01021973')
            celular = driver.find_element(By.ID, 'celular')
            celular.send_keys('(81)915975324')
            email = driver.find_element(By.ID, 'email')
            email.send_keys('thanos@joiadoinfinito.com')
            sleep(1)
            enviar = driver.find_element(By.ID, 'enviar')
            enviar.click()
            sleep(1)
            confirmar = driver.find_element(By.ID, 'confirmar')
            confirmar.click()
            sleep(1)
        cancelar = driver.find_element(By.ID, "cancelar")
        cancelar.click()
        sleep(1)

        # Teste para cadastrar faltando dado e com o email incorreto
        cadastrar_tutor = driver.find_element(By.ID, 'cadastrar_tutor')
        cadastrar_tutor.click()
        nome = driver.find_element(By.ID, 'nome')
        nome.send_keys('Visão')
        cpf = driver.find_element(By.ID, 'cpf')
        cpf.send_keys('178.654.258.44')
        data = driver.find_element(By.ID, 'dataNascimento')
        data.send_keys('01101968')
        celular = driver.find_element(By.ID, 'celular')
        celular.send_keys('(81)915975324')
        enviar = driver.find_element(By.ID, 'enviar')
        enviar.click()
        sleep(1)
        email = driver.find_element(By.ID, 'email')
        email.send_keys('visao@joiadamente')
        enviar = driver.find_element(By.ID, 'enviar')
        enviar.click()
        confirmar = driver.find_element(By.ID, 'confirmar')
        confirmar.click()
        sleep(1)
        email = driver.find_element(By.ID, 'email')
        email.send_keys('.com')
        sleep(5)
        enviar = driver.find_element(By.ID, 'enviar')
        enviar.click()
        sleep(5)
        confirmar = driver.find_element(By.ID, 'confirmar')
        confirmar.click()


        # adicionar um pet a um tutor cadastrado.
        dados = {'pets': ['', 'Tesseract', 'Groot'],
                 'raca': ['', 'Joia do espaço', 'Árvore'],
                 'data': ['', '01011990', '02021992']}
        driver.find_element(By.ID, '31').click()
        for i in range(3):
            if i != 1:
                driver.find_element(By.ID, 'cadastrar_pet').click()


            driver.find_element(By.ID, 'nomePet').clear()
            driver.find_element(By.ID, 'nomePet').send_keys(dados['pets'][i])
            driver.find_element(By.ID, 'especie').clear()
            driver.find_element(By.ID, 'especie').send_keys('Joia do Infinito')
            driver.find_element(By.ID, 'raca').clear()
            driver.find_element(By.ID, 'raca').send_keys(dados['raca'][i])
            driver.find_element(By.ID, 'dtNasc').clear()
            driver.find_element(By.ID, 'dtNasc').send_keys(dados['data'][i])
            driver.find_element(By.ID, 'sexo').click()
            driver.find_element(By.ID, 'peso').clear()
            driver.find_element(By.ID, 'peso').send_keys(60)
            driver.find_element(By.ID, 'porte').clear()
            driver.find_element(By.ID, 'porte').send_keys('Grande')
            sleep(2)

            driver.find_element(By.ID, 'enviar').click()
            sleep(1)
            if i != 0:
                driver.find_element(By.ID, 'confirmar').click()
        driver.close()






        



        

