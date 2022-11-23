import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec


def text_box_by_xpath(tiempo):
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    driver.implicitly_wait(15)
    """
    nombre = driver.find_element(By.XPATH,"//input[contains(@id,'userName')]")
    nombre.send_keys("Rodrigo")
    """
    driver.find_element(By.XPATH, "//input[contains(@id,'userName') and contains(@type,'text')]").send_keys("Alan")
    time.sleep(tiempo)
    driver.find_element(By.XPATH, "//input[contains(@id,'userEmail') and contains(@type,'email')]").send_keys("correo@gmail.com")
    time.sleep(tiempo)
    driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]").send_keys("Direccion 1")
    time.sleep(tiempo)
    driver.find_element(By.XPATH, "//textarea[contains(@id,'permanentAddress')]").send_keys("Direccion 2")
    time.sleep(tiempo)
    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(tiempo)
    driver.find_element(By.XPATH, "//button[contains(@id,'submit')]").click()
    time.sleep(tiempo)


def text_box_by_id(tiempo):
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    """
    nombre = driver.find_element(By.XPATH,"//input[contains(@id,'userName')]")
    nombre.send_keys("Rodrigo")
    """
    driver.find_element(By.ID, "userName").send_keys("Alan")
    time.sleep(tiempo)
    driver.find_element(By.ID, "userEmail").send_keys("correo@gmail.com")
    time.sleep(tiempo)
    driver.find_element(By.ID, "currentAddress").send_keys("Direccion tiempo")
    time.sleep(tiempo)
    driver.find_element(By.ID, "permanentAddress").send_keys("Direccion 2")
    time.sleep(tiempo)
    #  driver.execute_script("window.scrollTo(0,500)")
    #  time.sleep(tiempo)
    boton_aceptar = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", boton_aceptar)    #Se busca elemento haciendo scroll
    boton_aceptar.click()
    time.sleep(tiempo)
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(tiempo)


def espera_explicita(tiempo):
    # A URL that delays loading
    driver.get("https://www.chedraui.com.mx/compras-en-linea")
    driver.implicitly_wait(10)
    element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='openShoppingSelector'][contains(.,'Selecciona tu tienda')]")))
    element.click()
    time.sleep(tiempo)


def seleccionar_check(tiempo):
    driver.get("https://demoqa.com/elements")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//li[@class='btn btn-light '][contains(.,'Check Box')]").click()
    time.sleep(tiempo)
    driver.find_element(By.XPATH,"//span[@class='rct-title'][contains(.,'Home')]").click()
    time.sleep(tiempo)
    driver.find_element(By.XPATH, "//span[@class='rct-title'][contains(.,'Home')]").click()
    time.sleep(10)

def seleccionar_combobox(tiempo):
    driver.get("https://www.htmlquick.com/reference/tags/select.html")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0,2000)")

    puntero = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//select[contains(@name,'sport')]")))
    #puntero = driver.find_element(By.XPATH,"//select[contains(@name,'sport')]")
    seleccion = Select(puntero)
    seleccion.select_by_visible_text("Tennis")
    time.sleep(tiempo)
    seleccion.select_by_index(2)    # Mejor forma de seleccionar
    time.sleep(tiempo)
    driver.find_element(By.XPATH,"(//input[contains(@type,'submit')])[1]").click()
    time.sleep(10)


# Ejemplo para acceder a elementos dentro de un iFrame y so de select
def test_uanl(tiempo):
    try:
        driver.get("https://www.uanl.mx/enlinea/")
        driver.maximize_window()
        driver.implicitly_wait(10)

        # Acceder a un elementos dentro de un iframe#
        iframe = driver.find_element(By.XPATH, "//iframe[@name='loginbox']")
        driver.switch_to.frame(iframe)                          # switch to selected iframe

        puntero_tipo = driver.find_element(By.ID, 'tipo')       # Now click on button

        seleccion = Select(puntero_tipo)
        seleccion.select_by_index(0)    # Mejor forma de seleccionar
        time.sleep(tiempo)
        driver.find_element(By.ID, 'cuenta').send_keys("1747264")
        time.sleep(tiempo)
        driver.find_element(By.ID, 'pass').send_keys("")
        time.sleep(tiempo)
        driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Entrar')]").click()
        time.sleep(tiempo)
        driver.switch_to.alert.accept()
        time.sleep(10)
    except Exception as e:
        print(e)


#Acceder a un boton con interaccion javascript
def convertir_pdf(tiempo):
   driver.get("https://www.ilovepdf.com/es/word_a_pdf")
   driver.maximize_window()
   driver.implicitly_wait(10)
   esperar = WebDriverWait(driver, 10)

   try:
       puntero = esperar.until(ec.presence_of_element_located((By.XPATH, "//a[@id='pickfiles']")))
       puntero = driver.find_element(By.XPATH, "//a[@id='pickfiles']")
       time.sleep(tiempo)

       ruta = "C:/Users/GTIM/Downloads/Alan/@Programacion y edicion/PYTHON/_Entornos_virtuales/selenium/archivos/save.docx"
       file_tag_list = driver.find_elements(By.XPATH, "//input[@type = 'file']")    #   Elemento que funciona con un script #
       file_tag_list[0].send_keys(ruta)
       time.sleep(tiempo)

       xpath_descargar = "//button[contains(@id,'processTask')]"
       convertir = esperar.until(ec.element_to_be_clickable((By.XPATH, xpath_descargar)))
       convertir.click()
       time.sleep(tiempo)

       descargar = esperar.until(ec.element_to_be_clickable((By.ID, 'pickfiles')))
       descargar.click()
       time.sleep(5)

   except Exception as e:
       print(e)


def subir_archivos(tiempo):
   driver.get("https://demoqa.com/upload-download")
   driver.maximize_window()
   driver.implicitly_wait(10)

   try:
       xpath_seleccionar_documento = "//input[contains(@id,'uploadFile')]"
       print(1)
       puntero = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_seleccionar_documento)))
       print(2)
       puntero = driver.find_element(By.XPATH, xpath_seleccionar_documento)
       print(3)
       puntero.send_keys("C:/Users/GTIM/Downloads/Alan/@Programacion y edicion/PYTHON/_Entornos_virtuales/selenium/archivos/save.docx")
       print(4)
       '''
       time.sleep(tiempo)
       driver.find_element(By.XPATH, "//button[contains(@id,'processTask')]").click()
       print(5)
       xpath_descargar = "//a[contains(@id,'pickfiles')]"
       print(6)
       WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_descargar)))
       print(6)'''
       time.sleep(10)
   except Exception as e:
       print(e)


def practica_forms(tiempo):
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    driver.implicitly_wait(10)
    esperar = WebDriverWait(driver, 10)

    try:
        driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
        driver.find_element(By.XPATH, "//input[contains(@id,'firstName')]").send_keys("Alan" + Keys.TAB + "Monroy" + Keys.TAB + "cuenta99@gmail.com")
        time.sleep(tiempo)
        driver.find_element(By.XPATH, "//label[@for='gender-radio-1'][contains(.,'Male')]").click()
        time.sleep(tiempo)
        driver.find_element(By.XPATH, "//input[contains(@id,'userNumber')]").send_keys("8111901788" + Keys.TAB + "12 Dec 2022")
        time.sleep(tiempo)
        subject = driver.find_element(By.XPATH, "//input[contains(@id,'subjectsInput')]")
        subject.send_keys("999")
        time.sleep(tiempo)
        check_musica = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-3'][contains(.,'Music')]")
        driver.execute_script("arguments[0].click();", check_musica)
        time.sleep(tiempo)
        ruta = "C:/Users/GTIM/Downloads/Alan/@Programacion y edicion/PYTHON/_Entornos_virtuales/selenium/archivos/save.docx"
        driver.find_element(By.XPATH, "//input[contains(@id,'uploadPicture')]").send_keys(ruta)
        driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]").send_keys("Guadalupe, Nuevo Leon, Dos Rios, Rio Orinoco #1831")
        time.sleep(tiempo)
        puntero_tipo = driver.find_element(By.XPATH, "//input[contains(@id,'react-select-3-input')]")
        puntero_tipo.send_keys("NCR")
        #driver.execute_script("arguments[0].click();", select_city)
        #seleccion = Select(puntero_tipo)
        #seleccion.select_by_index(0)
        time.sleep(tiempo)
        #select_city.send_keys("Nodia")

        time.sleep(tiempo*5)
    except Exception as e:
        print(e)


def decargar_mp3(tiempo):
    driver.get("https://mp3converter.fr/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    esperar = WebDriverWait(driver, 10)

    try:
        url_video = "https://www.youtube.com/watch?v=_OYVhr4KNzw&list=PLqssRG1J0s5XPh1Mny7b6qps6d52QEZ-r&index=9"
        ventana = driver.current_window_handle
        print(f"ventana: {ventana}")
        input_url = esperar.until(ec.presence_of_element_located((By.XPATH, "//input[contains(@id,'url')]")))
        driver.find_element(By.XPATH, "//input[contains(@id,'url')]").send_keys(url_video)
        driver.find_element(By.XPATH, "//button[contains(@id,'submit')]").click()
        time.sleep(tiempo)
        for handle in driver.window_handles:
            if handle != ventana:
                print(handle)
                driver.switch_to.window(ventana)
                break

        #if driver.current_window_handle != ventana:
        #driver.switch_to.window(ventana)

        driver.switch_to.frame("iframe")
        boton_aceptar = driver.find_element(By.XPATH, "(//div[contains(.,'Download')])[11]")
        print(boton_aceptar)
        if boton_aceptar.is_displayed(): #.is_enabled()
            driver.execute_script("arguments[0].click();", boton_aceptar)
            #boton_aceptar.click()

        #driver.execute_script("arguments[0].scrollIntoView();", boton_aceptar)
        time.sleep(tiempo*5)
    except Exception as e:

        print(e)


def conseguir_text(tiempo):
    driver.get("https://apex.oracle.com/pls/apex/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    espera = WebDriverWait(driver, 10)

    try:
        driver.find_element(By.XPATH, "//button[contains(.,'Sign In')]").click()
        time.sleep(tiempo)
        error_div = driver.find_element(By.XPATH, "//div[@id='F4550_P1_COMPANY_error']")
        print(error_div.text)
        time.sleep(tiempo*5)
    except Exception as e:
        print(e)


#   Crear conexión a chrome     #
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


#text_box_by_xpath(tiempo=.1)
#text_box_by_id(tiempo=1)        #Scrollvar
#espera_explicita(tiempo=.1)
#seleccionar_check(tiempo=.1)
#seleccionar_combobox(tiempo=1)
#test_uanl(tiempo=1)            #Acceder a elementos dentro de un iFrame, manejo de alerts
#convertir_pdf(tiempo=1)        #Acceder a un boton con interaccion javascript
#practica_forms(tiempo=2)        #Uso de tabs
#decargar_mp3(tiempo=1)
conseguir_text(tiempo=1)

driver.close()  # Cerrar drive (chrome)