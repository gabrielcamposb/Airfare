from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

link = "https://www.google.com/travel/flights/search?tfs=CBwQAhorEgoyMDI1LTEyLTAxag0IAhIJL20vMDl3d2xqcg4IAxIKL20vMDN3OTY4NhorEgoyMDI1LTEyLTA5ag4IAxIKL20vMDN3OTY4NnINCAISCS9tLzA5d3dsakABQAFIAXABggELCP___________wGYAQE&hl=pt-BR&gl=BR"

try:
    browser.get(link)
    price_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "jLMuyc")))
    
    price = price_element.text
    today = datetime.now().strftime("%d/%m/%Y")
    
    print(f"Data: {today}")
    print(f"Preço encontrado: {price}")
    
    file_path = "price.txt"
    
    if os.path.exists(file_path):
        mode = "a"
    else:
        mode = "w"
    
    with open(file_path, mode) as file:
        file.write(f"Data: {today} - Preço: {price}\n")
    print(f"O preço foi salvo com sucesso em {file_path}")
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    browser.quit()