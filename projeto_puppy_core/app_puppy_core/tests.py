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

    # def teste_cadastro_email_incorreto(self): # Pode estar incorreto
    #     driver = set_up()
    #     driver.get('http://127.0.0.1:8000/homeAdm/')

    #     driver.find_element(By.ID, 'cadastrar_tutor').click()
    #     driver.find_element(By.ID, 'nome').send_keys('Visão')
    #     driver.find_element(By.ID, 'cpf').send_keys('178.654.258.44')
    #     driver.find_element(By.ID, 'dataNascimento').send_keys('01101968')
    #     driver.find_element(By.ID, 'celular').send_keys('(81)915975324')
    #     driver.find_element(By.ID, 'email').send_keys('visao@joiadamente')
    #     driver.find_element(By.ID, 'enviar').click()
    #     sleep(3)

    #     driver.find_element(By.ID, 'enviar').click()

    #     driver.close()
    

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
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')
        
        sleep(2)
        
        elements = driver.find_elements(By.ID, 'nome_tutor')
        
        expected_text1 = "Homem de Ferro"
        expected_text2 = "Tanos"

        element1 = elements[0]
        element2 = elements[1]
        
        assert element1.text == expected_text1 and element2.text == expected_text2
   

    def teste_ver_info_tutor(self):
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')
        
        sleep(2)
        
        driver.find_element(By.ID, 'nome_tutor').click()
        
        sleep(2)
        
        nome = driver.find_element(By.ID, 'nome_tutor')
        cpf = driver.find_element(By.ID, 'cpf_tutor')
        data = driver.find_element(By.ID, 'data_tutor')
        celular = driver.find_element(By.ID, 'celular_tutor')
        email = driver.find_element(By.ID, 'email_tutor')
        
        sleep(2)
        
        assert nome.text == "Nome: Homem de Ferro" and cpf.text == "CPF: 123.864.286-88" and data.text == "Data de nascimento: July 1, 1960"
        assert celular.text == "Celular: (81)946271597" and email.text == "Email: ironman@vingadores.com"
        
        
        

    def teste_dados_alterar_preenchidos(self):
        pass
    
    def teste_alterar_cadastro(self):
        pass
    
    def teste_alterar_cadastro_faltando_dados(self):
        pass

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
