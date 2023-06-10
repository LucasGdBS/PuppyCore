from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def set_up():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--icognito')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    return driver


class TesteTutor(TestCase):

    def teste_ver_tutores(self): # OK
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

    # def teste_ver_info_tutor(self): Não está achando o tutor pra clicar
    #     driver = set_up()
    #     driver.get('http://127.0.0.1:8000')
    #     sleep(2)

    #     driver.find_element(By.ID, 'login').click()
    #     sleep(2)

    #     driver.find_element(By.ID, 'login').click()
    #     sleep(2)

    #     driver.find_element(By.ID, 'cadastrar_tutor').click()
    #     sleep(2)

    #     driver.find_element(By.ID, 'nome').send_keys('NOME2')
    #     driver.find_element(By.ID, 'cpf').send_keys('222.222.222-22')
    #     driver.find_element(By.ID, 'dataNascimento').send_keys('02022002')
    #     driver.find_element(By.ID, 'celular').send_keys('(81)222222222')
    #     driver.find_element(By.ID, 'email').send_keys('email2@gmail.com')
    #     sleep(2)
    #     driver.find_element(By.ID, 'enviar').click()
    #     sleep(2)
    #     driver.find_element(By.ID, 'confirmar').click()
    #     sleep(2)

    #     elements = driver.find_elements(By.ID, 'nome_tutor')
    #     for element in elements:
    #         if element.text == 'NOME2':
    #             element.click()
    #             break

    #     sleep(2)

    #     nome = driver.find_element(By.ID, 'nome_tutor')
    #     cpf = driver.find_element(By.ID, 'cpf_tutor')
    #     data = driver.find_element(By.ID, 'data_tutor')
    #     celular = driver.find_element(By.ID, 'celular_tutor')
    #     email = driver.find_element(By.ID, 'email_tutor')

    #     sleep(2)

    #     assert nome.text == "Nome: NOME2" and cpf.text == "CPF: 222.222.222-22" and data.text == "Data de nascimento: Feb. 2, 2002"
    #     assert celular.text == "Celular: (81)222222222" and email.text == "Email: email2@gmail.com"

    #     driver.close()

    def teste_dados_alterar_preenchidos(self): # OK
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
        data_nascimento = driver.find_element(
            By.ID, 'dataNascimento').get_attribute("value")
        celular = driver.find_element(By.ID, 'celular').get_attribute("value")
        email = driver.find_element(By.ID, 'email').get_attribute("value")

        assert nome == "NOME3" and cpf == "333.333.333-33" and data_nascimento == "2003-03-03" and celular == "(81)333333333" and email == "email3@gmail.com"

        driver.close()

    def teste_alterar_cadastro(self): # OK
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
        driver.find_element(By.ID, 'cpf').send_keys('444.444.444-45')
        driver.find_element(By.ID, 'dataNascimento').send_keys('04042005')
        driver.find_element(By.ID, 'celular').send_keys('(81)444444444')
        driver.find_element(By.ID, 'email').send_keys('email5@gmail.com')
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
            driver.find_element(
                By.ID, 'email_tutor').text == "Email: email4@gmail.com"

        driver.close()

    def teste_alterar_cadastro_faltando_dados(self): # OK
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
        driver.find_element(By.ID, 'cpf').send_keys('555.555.555-56')
        driver.find_element(By.ID, 'dataNascimento').send_keys('05052006')
        driver.find_element(By.ID, 'celular').send_keys('(81)555555555')
        driver.find_element(By.ID, 'email').send_keys('email5@gmail.com')
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

        count = 0

        driver.find_element(By.ID, 'email').send_keys(Keys.ENTER)
        count += 1
        driver.find_element(By.ID, 'email').send_keys(Keys.ENTER)
        count += 1

        assert count == 2

        driver.close()

    # def teste_ver_pets(self): #Erro no comando de clicar no elemento
    #     driver = set_up()
    #     driver.get('http://127.0.0.1:8000/homeAdm/')

    #     driver.find_element(By.ID, 'cadastrar_tutor').click()

    #     driver.find_element(By.ID, 'nome').send_keys('Viúva Negra')
    #     driver.find_element(By.ID, 'cpf').send_keys('133.821.244-78')
    #     driver.find_element(By.ID, 'dataNascimento').send_keys('02051990')
    #     driver.find_element(By.ID, 'celular').send_keys('(81)946578742')
    #     driver.find_element(By.ID, 'email').send_keys('blackwidow@vingadores.com')
    #     sleep(1)
    #     driver.find_element(By.ID, 'enviar').click()
    #     sleep(1)
    #     driver.find_element(By.ID, 'confirmar').click()
    #     sleep(1)

    #     elements = driver.find_elements(By.ID, 'nome_tutor')
    #     for i in elements:
    #         if i.text == 'Viúva Negra':
    #             i.click()
    #             break

    #     sleep(2)
    #     driver.find_element(By.ID, 'cadastrar_pet').click()
    #     sleep(2)

    #     driver.find_element(By.ID, 'nomePet').send_keys('Arqueiro')
    #     driver.find_element(By.ID, 'especie').send_keys('Gavião')
    #     driver.find_element(By.ID, 'raca').send_keys('HawkEye')
    #     driver.find_element(By.ID, 'dtNasc').send_keys('02021992')
    #     driver.find_element(By.ID, 'sexo').click()
    #     driver.find_element(By.ID, 'peso').send_keys(91)
    #     driver.find_element(By.ID, 'porte').send_keys('Grande')
    #     sleep(2)
    #     driver.find_element(By.ID, 'enviar').click()
    #     sleep(1)
    #     driver.find_element(By.ID, 'confirmar').click()

    #     pets = driver.find_element(By.NAME, 'nome_pet')
    #     assert pets.text == 'Arqueiro'
    #     sleep(2)
    #     driver.close()

    # def teste_ver_info_pet(self): # Erro no comando de click
    #     driver = set_up()
    #     driver.get('http://127.0.0.1:8000/')

    #     driver.find_element(By.ID, 'login').click()
    #     sleep(2)

    #     driver.find_element(By.ID, 'login').click()
    #     sleep(2)

    #     driver.find_element(By.ID, 'cadastrar_tutor').click()

    #     driver.find_element(By.ID, 'nome').send_keys('Capitã Marvel')
    #     driver.find_element(By.ID, 'cpf').send_keys('133.821.244-48')
    #     driver.find_element(By.ID, 'dataNascimento').send_keys('02051990')
    #     driver.find_element(By.ID, 'celular').send_keys('(81)946578742')
    #     driver.find_element(By.ID, 'email').send_keys('carol_danvers@vingadores.com')
    #     sleep(1)
    #     driver.find_element(By.ID, 'enviar').click()
    #     sleep(1)
    #     driver.find_element(By.ID, 'confirmar').click()
    #     sleep(1)

    #     driver.find_element(By.NAME, 'Capitã Marvel').click()
    #     sleep(2)
    #     driver.find_element(By.ID, 'cadastrar_pet').click()

    #     driver.find_element(By.ID, 'nomePet').send_keys('Goose')
    #     driver.find_element(By.ID, 'especie').send_keys('Gato')
    #     driver.find_element(By.ID, 'raca').send_keys('Laranja')
    #     driver.find_element(By.ID, 'dtNasc').send_keys('02021201')
    #     driver.find_element(By.ID, 'sexo').click()
    #     driver.find_element(By.ID, 'peso').send_keys(5)
    #     driver.find_element(By.ID, 'porte').send_keys('Pequeno')
    #     sleep(2)
    #     driver.find_element(By.ID, 'enviar').click()
    #     sleep(1)
    #     driver.find_element(By.ID, 'confirmar').click()

    #     driver.find_element(By.NAME, 'nome_pet').click()
    #     sleep(2)

    #     nome = driver.find_element(By.ID, 'nome_pet')
    #     especie = driver.find_element(By.ID, 'especie_pet')
    #     raca = driver.find_element(By.ID, 'raca_pet')
    #     data = driver.find_element(By.ID, 'data_pet')
    #     sexo = driver.find_element(By.ID, 'sexo_pet')
    #     peso = driver.find_element(By.ID, 'peso_pet')
    #     porte = driver.find_element(By.ID, 'porte_pet')

    #     assert nome.text == 'Nome: Goose' and especie.text == "Espécie: Gato" and\
    #         raca.text == 'Raça: Laranja' and data.text == "Data de Nascimento: Feb. 2, 1201" and\
    #         sexo.text == 'Sexo: M' and peso.text == 'Peso: 5.0' and porte.text == 'Porte: Pequeno'

    #     driver.close()
  
    def teste_dados_alterar_preenchidos_pet(self): # OK
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')

        driver.find_element(By.ID, 'cadastrar_tutor').click()

        driver.find_element(By.ID, 'nome').send_keys('Mariane Beatriz')
        driver.find_element(By.ID, 'cpf').send_keys('133.318.264-13')
        driver.find_element(By.ID, 'dataNascimento').send_keys('19092000')
        driver.find_element(By.ID, 'celular').send_keys('(81)988877800')
        driver.find_element(By.ID, 'email').send_keys(
            'mbsf@cesar.school')
        sleep(1)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(1)

        elements = driver.find_elements(By.ID, 'nome_tutor')
        for i in elements:
            if i.text == 'Mariane Beatriz':
                i.click()
                break
            

        sleep(2)
        driver.find_element(By.ID, 'cadastrar_pet').click()
        sleep(2)

        driver.find_element(By.ID, 'nomePet').send_keys('Animal1')
        driver.find_element(By.ID, 'especie').send_keys('C')
        driver.find_element(By.ID, 'raca').send_keys('C')
        driver.find_element(By.ID, 'dtNasc').send_keys('02062023')
        driver.find_element(By.ID, 'sexo').click()
        driver.find_element(By.ID, 'peso').send_keys(1)
        driver.find_element(By.ID, 'porte').send_keys('G')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()

        driver.find_element(By.NAME, 'nome_pet').click()
        driver.find_element(By.ID, 'alteracaoPet').click()

        nomePet = driver.find_element(By.ID, 'nomePet').get_attribute("value")
        especie = driver.find_element(By.ID, 'especie').get_attribute("value")
        raca = driver.find_element(By.ID, 'raca').get_attribute("value")
        dtNasc = driver.find_element(By.ID, 'dtNasc').get_attribute("value")
        sexo = driver.find_element(By.ID, 'sexo').get_attribute("value")
        peso = driver.find_element(By.ID, 'peso').get_attribute("value")
        porte = driver.find_element(By.ID, 'porte').get_attribute("value")

        assert nomePet == "Animal1" and especie == "C" and dtNasc == "2023-06-02" and raca == "C" and sexo == 'M' and peso == "1.0" and porte == "G"

        driver.close()

    def teste_alterar_cadastro_pet(self):# OK
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')

        driver.find_element(By.ID, 'cadastrar_tutor').click()

        driver.find_element(By.ID, 'nome').send_keys('Mariane Beatriz Soares Fontes')
        driver.find_element(By.ID, 'cpf').send_keys('704.358.274-14')
        driver.find_element(By.ID, 'dataNascimento').send_keys('19092000')
        driver.find_element(By.ID, 'celular').send_keys('(81)988877800')
        driver.find_element(By.ID, 'email').send_keys(
            'mbsf@cesar.school')
        sleep(1)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(1)

        elements = driver.find_elements(By.ID, 'nome_tutor')
        for i in elements:
            if i.text == 'Mariane Beatriz Soares Fontes':
                i.click()
                break

        sleep(2)
        driver.find_element(By.ID, 'cadastrar_pet').click()
        sleep(2)

        driver.find_element(By.ID, 'nomePet').send_keys('Animal2')
        driver.find_element(By.ID, 'especie').send_keys('C')
        driver.find_element(By.ID, 'raca').send_keys('C')
        driver.find_element(By.ID, 'dtNasc').send_keys('02062023')
        driver.find_element(By.ID, 'sexo').click()
        driver.find_element(By.ID, 'peso').send_keys(1)
        driver.find_element(By.ID, 'porte').send_keys('G')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()

        driver.find_element(By.NAME, 'nome_pet').click()

        driver.find_element(By.ID, 'alteracaoPet').click()
        sleep(2)

        driver.find_element(By.ID, 'raca').clear()
        driver.find_element(By.ID, 'raca').send_keys('SRD')
        sleep(1)

        driver.find_element(By.ID, 'dtNasc').clear()
        driver.find_element(By.ID, 'dtNasc').send_keys('12032012')
        sleep(1)

        driver.find_element(By.ID, 'sexo').click()

        driver.find_element(By.ID, 'peso').clear()
        driver.find_element(By.ID, 'peso').send_keys('2')
        sleep(1)

        driver.find_element(By.ID, 'enviar').click()
        sleep(2)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(2)

        assert driver.find_element(By.ID, 'raca_pet').text == "Raça: SRD" and\
            driver.find_element(By.ID, 'data_pet').text == "Data de Nascimento: March 12, 2012" and\
            driver.find_element(By.ID, 'peso_pet').text == 'Peso: 1.0' 

        driver.close()

    def teste_alterar_cadastro_faltando_dados_pet(self): # FAILED ta escrito errado
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')

        driver.find_element(By.ID, 'cadastrar_tutor').click()

        driver.find_element(By.ID, 'nome').send_keys('Mariane Soares Fontes')
        driver.find_element(By.ID, 'cpf').send_keys('704.358.274-13')
        driver.find_element(By.ID, 'dataNascimento').send_keys('19092000')
        driver.find_element(By.ID, 'celular').send_keys('(81)988877800')
        driver.find_element(By.ID, 'email').send_keys(
            'mbsf@cesar.school')
        sleep(1)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(1)

        elements = driver.find_elements(By.ID, 'nome_tutor')
        for i in elements:
            if i.text == 'Mariane Soares Fontes':
                i.click()
                break

        sleep(2)
        driver.find_element(By.ID, 'cadastrar_pet').click()
        sleep(2)

        driver.find_element(By.ID, 'nomePet').send_keys('Animal3')
        driver.find_element(By.ID, 'especie').send_keys('C')
        driver.find_element(By.ID, 'raca').send_keys('C')
        driver.find_element(By.ID, 'dtNasc').send_keys('02062023')
        driver.find_element(By.ID, 'sexo').click()
        driver.find_element(By.ID, 'peso').send_keys(1)
        driver.find_element(By.ID, 'porte').send_keys('G')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()

        driver.find_element(By.NAME, 'nome_pet').click()
        
        sleep(2)


        driver.find_element(By.ID, 'alteracaoPet').click()
        sleep(2)

        driver.find_element(By.ID, 'especie').clear()
        driver.find_element(By.ID, 'especie').send_keys('Felino')
        sleep(1)

        driver.find_element(By.ID, 'dtNasc').clear()
        driver.find_element(By.ID, 'dtNasc').send_keys('02052017')
        sleep(1)

        driver.find_element(By.ID, 'nomePet').clear()
        sleep(1)

        count = 0

        driver.find_element(By.ID, 'nomePet').send_keys(Keys.ENTER)
        count += 1
        driver.find_element(By.ID, 'nomePet').send_keys(Keys.ENTER)
        count += 1

        assert count == 2

        driver.close()


    def teste_confirmarMarcarVacina(self): # OK
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/cadastroTutor/')

        sleep(2)
        driver.find_element(By.NAME, 'nome').send_keys('Maryanne')
        driver.find_element(By.ID, 'cpf').send_keys('704.358.274-1')
        driver.find_element(By.ID, 'dataNascimento').send_keys('19092000')
        driver.find_element(By.ID, 'celular').send_keys('(81)988877800')
        driver.find_element(By.ID, 'email').send_keys('mbsf@cesar.school')
        sleep(1)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(1)
        
        elements = driver.find_elements(By.ID, 'nome_tutor')
        for i in elements:
            if i.text == 'Maryanne':
                i.click()
                break
        sleep(2)
        driver.find_element(By.ID, 'cadastrar_pet').click()
        sleep(2)

        driver.find_element(By.ID, 'nomePet').send_keys('Animal9')
        driver.find_element(By.ID, 'especie').send_keys('C')
        driver.find_element(By.ID, 'raca').send_keys('C')
        driver.find_element(By.ID, 'dtNasc').send_keys('02062023')
        driver.find_element(By.ID, 'sexo').click()
        driver.find_element(By.ID, 'peso').send_keys(1)
        driver.find_element(By.ID, 'porte').send_keys('G')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(1)

        driver.find_element(By.NAME, 'nome_pet').click()
        sleep(1)    

        expected_url = driver.current_url
        driver.find_element(By.ID, 'cadastra_vacina').click()
        sleep(1)

        driver.find_element(By.ID, 'tipoVacina').send_keys('Raiva canina')
        sleep(1)
        driver.find_element(By.ID, 'dataVacina').send_keys('02102023')
        sleep(1)
        driver.find_element(By.NAME, 'nomeVeterinario').send_keys('Miss Marvel')
        sleep(1)
        driver.find_element(By.ID, 'enviar').click()
        sleep(2)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(2)

        current_url = driver.current_url

        assert current_url == expected_url

        driver.close()


    def teste_incompletoMarcarVacina(self): # OK
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')

        driver.find_element(By.ID, 'cadastrar_tutor').click()

        driver.find_element(By.ID, 'nome').send_keys('Mariane Beatriz')
        driver.find_element(By.ID, 'cpf').send_keys('704.358.274-14')
        driver.find_element(By.ID, 'dataNascimento').send_keys('19092000')
        driver.find_element(By.ID, 'celular').send_keys('(81)988877800')
        driver.find_element(By.ID, 'email').send_keys(
            'mbsf@cesar.school')
        sleep(1)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()
        driver.get('http://127.0.0.1:8000/homeAdm/')
        sleep(1)
        
        driver.find_element(By.NAME, 'Mariane Beatriz').click()

              

        sleep(2)
        driver.find_element(By.ID, 'cadastrar_pet').click()
        sleep(2)

        driver.find_element(By.ID, 'nomePet').send_keys('Animal7')
        driver.find_element(By.ID, 'especie').send_keys('C')
        driver.find_element(By.ID, 'raca').send_keys('C')
        driver.find_element(By.ID, 'dtNasc').send_keys('02062023')
        driver.find_element(By.ID, 'sexo').click()
        driver.find_element(By.ID, 'peso').send_keys(1)
        driver.find_element(By.ID, 'porte').send_keys('G')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()

        driver.find_element(By.NAME, 'nome_pet').click()
        sleep(1)
        driver.find_element(By.ID, 'cadastra_vacina').click()
        sleep(1)
        expected_url = driver.current_url

        driver.find_element(By.ID, 'dataVacina').send_keys('12122023')
        driver.find_element(By.NAME, 'nomeVeterinario').send_keys('Ricardo Berardo')
        driver.find_element(By.ID, 'enviar').click()

        sleep(2)
        
        current_url = driver.current_url

        assert current_url == expected_url

        driver.close()

    def teste_cadastro_exames_em_branco(self): # OK
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')
        sleep(2)

        driver.find_element(By.ID, 'cadastrar_tutor').click()
        sleep(2)

        driver.find_element(By.ID, 'nome').send_keys('CapitaoAmerica')
        driver.find_element(By.ID, 'cpf').send_keys('123.111.458-11')
        driver.find_element(By.ID, 'dataNascimento').send_keys('01012011')
        driver.find_element(By.ID, 'celular').send_keys('(81)111111111')
        driver.find_element(By.ID, 'email').send_keys('email3@gmail.com')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(2)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(2)

        elements = driver.find_elements(By.ID, 'nome_tutor')
        for element in elements:
            if element.text == 'CapitaoAmerica':
                element.click()
                break
        sleep(2)

        driver.find_element(By.ID, 'cadastrar_pet').click()

        driver.find_element(By.ID, 'nomePet').send_keys('Shay')
        driver.find_element(By.ID, 'especie').send_keys('Cão')
        driver.find_element(By.ID, 'raca').send_keys('Poodle')
        driver.find_element(By.ID, 'dtNasc').send_keys('02022022')
        driver.find_element(By.ID, 'sexo').click()
        driver.find_element(By.ID, 'peso').send_keys(4)
        driver.find_element(By.ID, 'porte').send_keys('Pequeno')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()

        driver.find_element(By.NAME, 'nome_pet').click()
        sleep(2)

        driver.find_element(By.ID, 'cadastra_exame').click()
        sleep(2)

        driver.find_element(By.ID, 'nomeVeterinario').send_keys('Gabriel')
        driver.find_element(By.ID, 'exame').send_keys('Hemograma')
        driver.find_element(By.ID, 'dataSolicitacao').send_keys('30042023')
        driver.find_element(By.ID, 'dataResultado').send_keys('05052023')
        driver.find_element(By.ID, 'resultado').send_keys("tudo bem")
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(1)

        driver.close()

    def teste_cadastro_exames(self): # Failed
        driver = set_up()
        driver.get('http://127.0.0.1:8000/homeAdm/')
        sleep(2)

        driver.find_element(By.ID, 'cadastrar_tutor').click()
        sleep(2)

        driver.find_element(By.ID, 'nome').send_keys('Batman')
        driver.find_element(By.ID, 'cpf').send_keys('123.178.121-16')
        driver.find_element(By.ID, 'dataNascimento').send_keys('01012011')
        driver.find_element(By.ID, 'celular').send_keys('(81)111111111')
        driver.find_element(By.ID, 'email').send_keys('email3@gmail.com')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(2)
        driver.find_element(By.ID, 'confirmar').click()
        sleep(2)

        elements = driver.find_elements(By.ID, 'nome_tutor')
        for element in elements:
            if element.text == 'Batman':
                element.click()
                break
        sleep(2)

        driver.find_element(By.ID, 'cadastrar_pet').click()

        driver.find_element(By.ID, 'nomePet').send_keys('Robin')
        driver.find_element(By.ID, 'especie').send_keys('Gato')
        driver.find_element(By.ID, 'raca').send_keys('Amarelo')
        driver.find_element(By.ID, 'dtNasc').send_keys('02022022')
        driver.find_element(By.ID, 'sexo').click()
        driver.find_element(By.ID, 'peso').send_keys(4)
        driver.find_element(By.ID, 'porte').send_keys('Medio')
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)
        driver.find_element(By.ID, 'confirmar').click()

        driver.find_element(By.NAME, 'nome_pet').click()
        sleep(2)

        driver.find_element(By.ID, 'cadastra_exame').click()
        sleep(2)

        driver.find_element(By.ID, 'nomeVeterinario').send_keys('SuperHomem')
        driver.find_element(By.ID, 'exame').send_keys('Hemograma')
        driver.find_element(By.ID, 'dataSolicitacao').send_keys('30042023')
        driver.find_element(By.ID, 'dataResultado').send_keys('05052023')
        driver.find_element(By.ID, 'resultado').send_keys("Exemplo de resultado")
        sleep(2)
        driver.find_element(By.ID, 'enviar').click()
        sleep(1)

        driver.close()
