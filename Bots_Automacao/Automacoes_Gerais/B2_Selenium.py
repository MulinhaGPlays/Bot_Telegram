from selenium import webdriver # importando o webdriver do selenium para automação de interação com o navegador
from webdriver_manager.chrome import ChromeDriverManager # importando o ChromeDriverManager do webdriver_manager para automação de interação com o navegador
from selenium.webdriver.chrome.service import Service # importando o Service do selenium para automação de interação com o navegador
import time # Importa o time para ajustar o tempo de espera

servico = Service(ChromeDriverManager().install()) # Inicia o serviço do ChromeDriver
navegador = webdriver.Chrome(service=servico) # Inicia o navegador do ChromeDriver
navegador.get("http://warezcdn.net/listing.php?type=movies") # Escreve o endereço do site no navegador
navegador.find_element('xpath', '//*[@id="example_filter"]/label/input').send_keys("The Matrix") # Digita o nome do filme no campo de busca
time.sleep(2) # Ajusta o tempo de espera
navegador.find_element('xpath', '//*[@id="example"]/tbody/tr/td[4]/a').click() # Clica no botão de busca
time.sleep(5) # Ajusta o tempo de espera