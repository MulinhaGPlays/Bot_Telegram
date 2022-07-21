from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("http://warezcdn.net/listing.php?type=movies")
navegador.find_element('xpath', '//*[@id="example_filter"]/label/input').send_keys("The Matrix")
time.sleep(2)
navegador.find_element('xpath', '//*[@id="example"]/tbody/tr/td[4]/a').click()
time.sleep(5)