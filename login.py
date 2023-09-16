from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def login_gov():
    # Inicialize o driver do navegador (no exemplo, usaremos o Chrome)
    driver = webdriver.Chrome()

    # Abra o site
    driver.get("https://portalservicos.senatran.serpro.gov.br/#/infracoes/consultar/veiculo")

    time.sleep(5)

    # Localize o elemento pelo ID
    usuario = driver.find_element(By.ID, "accountId")
    usuario.send_keys('LOGIN')

    btnContinuar = driver.find_element(By.CLASS_NAME, "button-continuar")
    btnContinuar.click()

    time.sleep(6)

    senha = driver.find_element(By.ID, "password")
    senha.send_keys("SENHA")

    btnEntrar = driver.find_element(By.ID, "submit-button")
    btnEntrar.click()

    time.sleep(6)

    # Feche o navegador
    driver.quit()

