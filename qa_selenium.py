import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec


def test_links(tiempo):
    driver.get("https://www.youtube.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    esperar = WebDriverWait(driver, 10)

    #Obtener todos los links de la pagina
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"El numeor de link de la pagina es: {len(links)}")

    # CREAR NUEVA PESTAÑA #
    """
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.indeed.com/career-advice/career-development/types-of-personality-test')"""

    for num in links:
        if num.text != '':
            print(num.text)

    driver.find_element(By.LINK_TEXT, "Biblioteca").click()
    time.sleep(tiempo)



#   Crear conexión a chrome     #
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

#  FUNCIONES #
test_links(tiempo=1)

driver.close()