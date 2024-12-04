from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#importo el metodo que esta dentro del archivo sesion.py 
from test_case.sesion import insertar_usuario_contrasena
import time


class TestCategorias:
     def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost/Ventas/login/')
    
     def teardown_method(self):
        self.driver.quit()
        print("  Paso prueba")
    
     def test_desplegar_categorias(self):
        #importamos la clase de sesion.py
        insertar_usuario_contrasena(self.driver)
        #Desplegamos el menu del boton categorias
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Categorías')]").click()
        time.sleep(1)
        #seleccionamos el boton Listado de categoriuas
        self.driver.find_element(By.XPATH, "//a[@class='nav-link']//p[contains(text(),'Listado de categorías')]").click()
        time.sleep(1)
         # Verifica  que el contenido este ahi lista categorias
        actual = self.driver.find_element(By.XPATH, "//div[contains(@class,'container-fluid')]//h1").text
        esperado = "Listado de Categorías"
        print("********", actual)
        assert esperado in actual, f"Error. Actual: {actual}, Esperado: {esperado}"
        time.sleep(2)
     
     def test_crear_categoria(self):
        ################## creamos una nueva categoria
        ################## mover a una clase independiete para el test
        insertar_usuario_contrasena(self.driver)
        #Desplegamos el menu del boton categorias
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Categorías')]").click()
        time.sleep(1)
        #seleccionamos el boton Listado de categoriuas
        self.driver.find_element(By.XPATH, "//a[@class='nav-link']//p[contains(text(),'Listado de categorías')]").click()
        time.sleep(1)
        #click al boton nueva categoria
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']//i").click()
        #time.sleep(1)
        ########################
        ## agregamos nueva categoria ##
        #self.driver.find_element(By.XPATH, "//input[@id='nombre_categoria']").send_keys("Repuestos")
        #time.sleep(2)
        ## guardamos la nueva categoria 
        #self.driver.find_element(By.XPATH, "//button[@id='btn_create']").click()
        #time.sleep(2)
        #verificamos que la categoria nueva que agregamos este agregada
        self.driver.find_element(By.XPATH, "//a[text()='4']").click()
        time.sleep(1)
        actual = self.driver.find_element(By.XPATH, "//tr[@class='odd']//td[contains(text(),'Repuestos')]").text
        esperado = "Repuestos"
        print("********", actual)
        assert esperado in actual, f"Error. Actual: {actual}, Esperado: {esperado}"
        time.sleep(2)