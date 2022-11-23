import time
from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

def navegar_entre_paginas():
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(1)
    driver.get("https://www.youtube.com/")
    time.sleep(1)
    driver.get("https://www.w3schools.com/python/numpy/numpy_array_shape.asp")
    time.sleep(1)
    driver.execute_script("window.history.go(-1)")
    time.sleep(1)
    driver.execute_script("window.history.go(-1)")
    time.sleep(1)
    driver.execute_script("window.history.go(2)")

#   Crear conexión a chrome     #
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
t=1

navegar_entre_paginas()

time.sleep(2)
driver.close()