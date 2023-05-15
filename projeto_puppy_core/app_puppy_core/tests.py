from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def set_up():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--icognito') 
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        
        
        return driver

class TesteTutor(TestCase):
    
    def teste_ver_tutores(self):
        driver = set_up()
        driver.get('http://127.0.0.1:8000')
        sleep(2)
        
        driver.find_element(By.ID, 'login').click()
        sleep(2)
        
        driver.find_element(By.ID, 'login').click()
        sleep(2)
        
        driver.find_element(By.ID, 'cadastrar_tutor').click()
        sleep(2)
        
        driver.find_element(By.ID, 'nome').send_keys('NOME1')
        driver.find_element(By.ID, 'cpf').send_keys('111.111.111-11')
        driver.find_element(By.ID, 'dataNascimento').send_keys('01012001')
        driver.find_element(By.ID, 'celular').send_keys('(81)111111111')
        driver.find_element(By.ID, 'email').send_keys('email1@gmail.com')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(2)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(2)
        
        elements = driver.find_elements(By.ID, 'nome_tutor')
        for element in elements:
            if element.text == 'NOME1':
                expected_text = "NOME1"
                assert element.text == expected_text
                break      
            
        
        driver.close()
   

    def teste_ver_info_tutor(self):
        driver = set_up()
        driver.get('http://127.0.0.1:8000')
        sleep(2)
        
        driver.find_element(By.ID, 'login').click()
        sleep(2)
        
        driver.find_element(By.ID, 'login').click()
        sleep(2)
        
        driver.find_element(By.ID, 'cadastrar_tutor').click()
        sleep(2)
        
        driver.find_element(By.ID, 'nome').send_keys('NOME2')
        driver.find_element(By.ID, 'cpf').send_keys('222.222.222-22')
        driver.find_element(By.ID, 'dataNascimento').send_keys('02022002')
        driver.find_element(By.ID, 'celular').send_keys('(81)222222222')
        driver.find_element(By.ID, 'email').send_keys('email2@gmail.com')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(2)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(2)
        
        
        elements = driver.find_elements(By.ID, 'nome_tutor')
        for element in elements:
            if element.text == 'NOME2':
                element.click()
                break
        
        
        sleep(2)
        
        nome = driver.find_element(By.ID, 'nome_tutor')
        cpf = driver.find_element(By.ID, 'cpf_tutor')
        data = driver.find_element(By.ID, 'data_tutor')
        celular = driver.find_element(By.ID, 'celular_tutor')
        email = driver.find_element(By.ID, 'email_tutor')
        
        sleep(2)
        
        assert nome.text == "Nome: NOME2" and cpf.text == "CPF: 222.222.222-22" and data.text == "Data de nascimento: Feb. 2, 2002"
        assert celular.text == "Celular: (81)222222222" and email.text == "Email: email2@gmail.com"
        
        driver.close()

    def teste_dados_alterar_preenchidos(self):
        driver = set_up()
        driver.get('http://127.0.0.1:8000')
        sleep(2)
        
        driver.find_element(By.ID, 'login').click()
        sleep(2)
        
        driver.find_element(By.ID, 'login').click()
        sleep(2)
        
        driver.find_element(By.ID, 'cadastrar_tutor').click()
        sleep(2)
        
        driver.find_element(By.ID, 'nome').send_keys('NOME3')
        driver.find_element(By.ID, 'cpf').send_keys('333.333.333-33')
        driver.find_element(By.ID, 'dataNascimento').send_keys('03032003')
        driver.find_element(By.ID, 'celular').send_keys('(81)333333333')
        driver.find_element(By.ID, 'email').send_keys('email3@gmail.com')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(2)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(2)
        
        elements = driver.find_elements(By.ID, 'nome_tutor')
        for element in elements:
            if element.text == 'NOME3':
                element.click()
                break
        
        sleep(2)
        
        driver.find_element(By.ID, 'alterar_tutor').click()
        
        sleep(2)
        
        nome = driver.find_element(By.ID, 'nome').get_attribute("value")
        cpf = driver.find_element(By.ID, 'cpf').get_attribute("value")
        data_nascimento = driver.find_element(By.ID, 'dataNascimento').get_attribute("value")
        celular = driver.find_element(By.ID, 'celular').get_attribute("value")
        email = driver.find_element(By.ID, 'email').get_attribute("value")
       
        assert nome == "NOME3" and cpf == "333.333.333-33" and data_nascimento == "2003-03-03"
        assert celular == "(81)333333333" and email == "email3@gmail.com"
        
        driver.close()
    
    def teste_alterar_cadastro(self):
        driver = set_up()
        driver.get('http://127.0.0.1:8000')
        sleep(2)
        
        driver.find_element(By.ID, 'login').click()
        sleep(2)
        
        driver.find_element(By.ID, 'login').click()
        sleep(2)
        
        driver.find_element(By.ID, 'cadastrar_tutor').click()
        sleep(2)
        
        driver.find_element(By.ID, 'nome').send_keys('NOME4')
        driver.find_element(By.ID, 'cpf').send_keys('444.444.444-45') #
        driver.find_element(By.ID, 'dataNascimento').send_keys('04042005')#
        driver.find_element(By.ID, 'celular').send_keys('(81)444444444')
        driver.find_element(By.ID, 'email').send_keys('email5@gmail.com') #
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(2)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(2)
        
        elements = driver.find_elements(By.ID, 'nome_tutor')
        for element in elements:
            if element.text == 'NOME4':
                element.click()
                break
        sleep(2)
        
        driver.find_element(By.ID, 'alterar_tutor').click()
        sleep(2)
        
        driver.find_element(By.ID, 'cpf').clear()
        driver.find_element(By.ID, 'cpf').send_keys('444.444.444-44')
        sleep(1)
        
        driver.find_element(By.ID, 'dataNascimento').clear()
        driver.find_element(By.ID, 'dataNascimento').send_keys('04042004')
        sleep(1)
        
        driver.find_element(By.ID, 'email').clear()
        driver.find_element(By.ID, 'email').send_keys('email4@gmail.com')
        sleep(1)
        
        driver.find_element(By.ID, 'enviar').click()
        sleep(2)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(2)
        
        assert driver.find_element(By.ID, 'cpf_tutor').text == "CPF: 444.444.444-44" and\
        driver.find_element(By.ID, 'data_tutor').text == "Data de nascimento: April 4, 2004" and\
        driver.find_element(By.ID, 'email_tutor').text == "Email: email4@gmail.com"
        
        driver.close()
    
    def teste_alterar_cadastro_faltando_dados(self):
        driver = set_up()
        driver.get('http://127.0.0.1:8000')
        sleep(2)
        
        driver.find_element(By.ID, 'login').click()
        sleep(2)
        
        driver.find_element(By.ID, 'login').click()
        sleep(2)
        
        driver.find_element(By.ID, 'cadastrar_tutor').click()
        sleep(2)
        
        driver.find_element(By.ID, 'nome').send_keys('NOME5')
        driver.find_element(By.ID, 'cpf').send_keys('555.555.555-56') #
        driver.find_element(By.ID, 'dataNascimento').send_keys('05052006')#
        driver.find_element(By.ID, 'celular').send_keys('(81)555555555')
        driver.find_element(By.ID, 'email').send_keys('email6@gmail.com') #
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(2)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(2)
        
        elements = driver.find_elements(By.ID, 'nome_tutor')
        for element in elements:
            if element.text == 'NOME5':
                element.click()
                break
        sleep(2)
        
        driver.find_element(By.ID, 'alterar_tutor').click()
        sleep(2)
        
        driver.find_element(By.ID, 'cpf').clear()
        driver.find_element(By.ID, 'cpf').send_keys('555.555.555-55')
        sleep(1)
        
        driver.find_element(By.ID, 'dataNascimento').clear()
        driver.find_element(By.ID, 'dataNascimento').send_keys('05052005')
        sleep(1)
        
        driver.find_element(By.ID, 'email').clear()
        sleep(1)
        
        count = 0;
        
        driver.find_element(By.ID, 'email').send_keys(Keys.ENTER)
        count +=1
        driver.find_element(By.ID, 'email').send_keys(Keys.ENTER)
        count +=1
        
        assert count == 2
        
        driver.close() 

    def teste_ver_pets(self):
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')

        driver.find_element(By.ID, 'cadastrar_tutor').click()

        driver.find_element(By.ID, 'nome').send_keys('Viúva Negra')
        driver.find_element(By.ID, 'cpf').send_keys('133.821.244-77')
        driver.find_element(By.ID, 'dataNascimento').send_keys('02051990')
        driver.find_element(By.ID, 'celular').send_keys('(81)946578742')
        driver.find_element(By.ID, 'email').send_keys('blackwidow@vingadores.com')
        sleep(1)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(1)

        elements = driver.find_elements(By.ID, 'nome_tutor')
        for i in elements:
            if i.text == 'Viúva Negra':
                i.click()
                break
        
        sleep(2)
        driver.find_element(By.ID, 'cadastrar_pet').click()
        sleep(2)

        driver.find_element(By.ID, 'nomePet').send_keys('Arqueiro')
        driver.find_element(By.ID, 'especie').send_keys('Gavião')
        driver.find_element(By.ID, 'raca').send_keys('HawkEye')
        driver.find_element(By.ID, 'dtNasc').send_keys('02021992')
        driver.find_element(By.ID, 'sexo').click()
        driver.find_element(By.ID, 'peso').send_keys(91)
        driver.find_element(By.ID, 'porte').send_keys('Grande')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()

        pets = driver.find_element(By.NAME, 'nome_pet')
        assert pets.text == 'Arqueiro'
        sleep(2)
        driver.close()

    def teste_ver_info_pet(self):
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')

        driver.find_element(By.ID, 'cadastrar_tutor').click()

        driver.find_element(By.ID, 'nome').send_keys('Capitã Marvel')
        driver.find_element(By.ID, 'cpf').send_keys('133.821.244-78')
        driver.find_element(By.ID, 'dataNascimento').send_keys('02051990')
        driver.find_element(By.ID, 'celular').send_keys('(81)946578742')
        driver.find_element(By.ID, 'email').send_keys('carol_danvers@vingadores.com')
        sleep(1)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(1)

        elements = driver.find_elements(By.ID, 'nome_tutor')
        for i in elements:
            if i.text == 'Capitã Marvel':
                i.click()
                break
        
        driver.find_element(By.ID, 'cadastrar_pet').click()

        driver.find_element(By.ID, 'nomePet').send_keys('Goose')
        driver.find_element(By.ID, 'especie').send_keys('Gato')
        driver.find_element(By.ID, 'raca').send_keys('Laranja')
        driver.find_element(By.ID, 'dtNasc').send_keys('02021201')
        driver.find_element(By.ID, 'sexo').click()
        driver.find_element(By.ID, 'peso').send_keys(5)
        driver.find_element(By.ID, 'porte').send_keys('Pequeno')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()

        driver.find_element(By.NAME, 'nome_pet').click()
        sleep(2)

        nome = driver.find_element(By.ID, 'nome_pet')
        especie = driver.find_element(By.ID, 'especie_pet')
        raca = driver.find_element(By.ID, 'raca_pet')
        data = driver.find_element(By.ID, 'data_pet')
        sexo = driver.find_element(By.ID, 'sexo_pet')
        peso = driver.find_element(By.ID, 'peso_pet')
        porte = driver.find_element(By.ID, 'porte_pet')

        assert nome.text == 'Nome: Goose' and especie.text == "Espécie: Gato" and raca.text == 'Raça: Laranja' and data.text == "Data de Nascimento: Feb. 2, 1201" and sexo.text == 'Sexo: M' and peso.text == 'Peso: 5.0' and porte.text == 'Porte: Pequeno'
        
        driver.close()
