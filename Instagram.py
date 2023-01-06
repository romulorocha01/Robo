from genericpath import exists
from selenium import webdriver
import time

navegador = webdriver.Chrome("chromedriver.exe")

# Acessar site
navegador.get("https://www.instagram.com/")
time.sleep(2)

# Logar no Insta
username = "robodahotmart"
password = "apenasumrobo"
apresentacao = "Olá, tudo certo? Antes de mais nada, gostaria de me apresentar. Sou sim um robô, fui desenvolvido por @romulo_rochaa. Então, não se preocupe, não sou golpe ou algo do tipo. Caso queira confirmar, pode me chamar no meu perfil particular, estarei te aguardando lá ;)"
curso = "Agora, falando um pouquinho sobre o curso, é o curso mais completo que você encontrará e o que mais teve alunas em 2021! (MAIS DE DUAS MIL ALUNAS). Após sua inscrição você receberá um link de acesso para assistir as aulas pelo seu celular, notebook, computador, tablet, etc. Você pode rever as aulas quantas vezes quiser e pelo tempo que precisar."
link = "Para saber mais, acesse o link e venha mudar de vida!!! https://go.hotmart.com/Y74744421T"
micro = "#micropigmentação"


navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[3]').click()
time.sleep(5)

# Clicar em "Agora Nao"
navegador.find_element('xpath', '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(1)

navegador.find_element('xpath','/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
time.sleep(3)

###########################################################################################################
def pesquisar1():

# Tela inicial
    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[1]/div[1]/a/div/div').click()
    time.sleep(4)
# Acessar pequisa
    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div/div[4]').click()
    time.sleep(2)

# Pesquisar a hashtag
    hashtag = micro

    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[1]').click()
    time.sleep(2)

    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[1]/input').send_keys(hashtag)
    time.sleep(3)

# Selecionar segunda opção
    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[1]/div[3]/div/div[1]/div/div[1]/div').click()
    time.sleep(5)
###########################################################################################################

def mandarMensagem():
# Clicar no primeiro post
    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div/div[1]/div[1]').click()
    time.sleep(4)

# Clicar no perfil
    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/h2').click()
    time.sleep(7)

# Clicar em "Enviar mensagem"
    try: 
        navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]').click()      
        time.sleep(5)
    except:
        pesquisar1()

    try:
        navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[4]/div[2]/div/div/div/div/div/div/div/div/span').click()
        # Voltar para a página inicial
        navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[1]/div/div[1]/div[1]/a/div/div').click()
        time.sleep(4)
    except:
        ""

# Escrever mensagem
    try:
        navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(apresentacao)
        time.sleep(3)

        navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]').click()
        time.sleep(4)

# Clicar na mensagem 
    #navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]').click()
# Escrever mensagem
        navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(curso)
        time.sleep(3)

        navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]').click()
        time.sleep(4)

# Clicar na mensagem 
    #navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]').click()
# Escrever mensagem
        navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(link)
        time.sleep(3)

        navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]').click()
        time.sleep(4)
    except:
        pesquisar1()

# Voltar para a página inicial
    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[1]/div/div[1]/div[1]/a/div/div').click()
    time.sleep(4)

    pesquisar1()

###########################################################################################################

def pesquisa2():
    # Acessar pequisa
    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[1]/div/div[2]/div/div[4]').click()
    time.sleep(2)

# Pesquisar a hashtag
    hashtag = "#empreendedorismo"

    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[1]').click()
    time.sleep(2)

    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[1]/input').send_keys(hashtag)
    time.sleep(3)
    
# Selecionar segunda opção
    navegador.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[1]/div[3]/div/div[1]/div/div[2]/div').click()
    time.sleep(5)

    mandarMensagem()

###########################################################################################################

i = 0
while (i <= 100): 
    pesquisar1()
    mandarMensagem()
    i = i + 1
    time.sleep(10)
else:
    print("Foram enviadas 100 mensagens")

###################################################################################################################
