import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\DELL\Desktop\geckodriver\geckodriver.exe")


    def login(self):
        driver = self.driver
        driver.get("https://instagram.com/")
        time.sleep(4)
        botao_login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        botao_login.click()
        time.sleep(3)
        campo_usuario = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        campo_usuario.click()
        time.sleep(3)
        campo_usuario.clear()
        time.sleep(3)
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        campo_senha.click()
        time.sleep(3)
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(15)
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        self.comente_nas_fotos_com_a_hashtag()

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        print("Digitando comentario")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 2))

    def comente_nas_fotos_com_a_hashtag(self):
        a = 0
        while (1):
            sorteio_quinhentos = "https://www.instagram.com/p/CW3TUR2JofM/"
            sorteio_pix = "https://www.instagram.com/p/CW5-DB8rieE/"

            ##Nessa lista de sorteios, você insere todos as variáveis que você criou acima.
            sorteios = [
                sorteio_quinhentos,
                sorteio_pix
            ]

            sorteio_da_vez = random.choice(sorteios)
            driver = self.driver
            time.sleep(5)
            driver.get(sorteio_da_vez)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:

                comments = [
                    "@ingridbrito1",
                    "@phaela_marques",
                    "@franciellelys",
                    "@muury_martins",
                    "@leticia.streit",
                    "@leeh_defreitas",
                    "@_t.dias",
                    "@laendriaferreira",
                    "@caio__franco",
                    "@alinedeoliveira_2020ok",
                    "@akira.ane",
                    "@julia.mendes._",
                    "@sl.surtada.ff",
                    "@markin_ws",
                    "@Beccafrancos2",
                    "@jovemg.m",
                    "@philipee_gomes",
                    "@biapow",
                    "@souzinha305",
                    "@claudinho251",
                    "@darsonhaily",
                    "@lakalaerafagi",
                    "@quelleanjos",
                    "@milahpetri",
                    "@fa.bioramos",
                    "@tatianeberger29",
                    "@bolsanell0",
                    "@elsadealbuquerque21",
                    "@rosasena___",
                    "@papai_dajulia",
                    "@restaurante.d.negreiros",
                    "@__mari.borges__",
                    "@souzamily3",
                    "@ijsilva38.78",
                    "@giovanna_maressa",
                    "@marinamagac",
                    "@xavierhellen35",
                    "@jovemsonhador2007",
                    "@luana_chellis",
                    "@sapolonini",
                    "@natii.baratto",
                    "@aldovictor2021",
                    "@biancadenardi_",
                    "@elizangela.tomaz.98",
                    "@pai_da_princesa07",
                    "@taninhacakesamor",
                    "@bruninha2073",
                    "@matheus_morais68",
                    "@galeno.camila",
                    "@mica._.messias____",
                    "@bellygomes_",
                    "@jainne__torres",
                    "@cxcheada",
                    "@mariasousa5980",
                    "@nathalialimarojas",
                    "@_rhaulcampos"



                ]
                frases = [
                    "Amém"
                ]

                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(1, 15))

                frase_da_vez = random.choice(frases)
                pessoa_1 = random.choice(comments)
                pessoa_2 = random.choice(comments)
                pessoa_3 = random.choice(comments)
                marcar_2_pessoas = pessoa_1 + " " + pessoa_2
                marcar_1_pessoa = frase_da_vez + " " + pessoa_1
               
                if sorteio_da_vez == sorteio_quinhentos:
                    self.type_like_a_person(marcar_1_pessoa, comment_input_box)
                    print("Comentei: ", marcar_1_pessoa, " no post: ", sorteio_da_vez, "")
               if sorteio_da_vez == sorteio_quinhentos:
                    self.type_like_a_person(marcar_1_pessoa, comment_input_box)
                    print("Comentei: ", marcar_1_pessoa, " no post: ", sorteio_da_vez, "")'''''
                time.sleep(random.randint(1, 10))
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()
                a = a + 1
               
                print('Vezes comentadas:')
                print(a)
                # A linha abaixo foi colocada a partir de uma sugestão no Youtube. Ela pode ser removida, caso você queira.
                for i in range(1, 3): driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(40)

                print(e)
                time.sleep(5)
RhaulBot = InstagramBot('usuario','senha')
RhaulBot.login()
