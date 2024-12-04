from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#importo el metodo que esta dentro del archivo sesion.py 
from test_case.sesion import insertar_usuario_contrasena
import time

class TestAlmacen:
     def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost/Ventas/login/')
    
     def teardown_method(self):
        self.driver.quit()
        print("  Paso prueba")
     
     def test_desplegar_almacen(self):
        #importamos la clase de sesion.py
        insertar_usuario_contrasena(self.driver)
        #Desplegamos el menu del boton .almacen
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Almacén')]").click()
        time.sleep(1)
        #seleccionamos el boton Listado de almacen
        self.driver.find_element(By.XPATH, "//a[@class='nav-link']//p[contains(text(),'Listado de productos')]").click()
        time.sleep(1)
        # Verifica  que el contenido este ahi lista de productos
        actual = self.driver.find_element(By.XPATH, "//div[contains(@class,'container-fluid')]//h1").text
        esperado = "Listado de productos"
        print("********", actual)
        assert esperado in actual, f"Error. Actual: {actual}, Esperado: {esperado}"


         #volvemos a desplegar el menu y seleccionamos almacen
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Almacén')]").click()
        time.sleep(1)
        #seleccionamos el boton creacion de productos
        self.driver.find_element(By.XPATH, "//a[@class='nav-link']//p[contains(text(),'Creación de productos')]").click()
        time.sleep(1)
        #verificamos que el titulo Resgitro de nuevo producto este ahi
        actual = self.driver.find_element(By.XPATH, "//div[contains(@class,'container-fluid')]//h1").text
        esperado = "Registro de un nuevo producto"
        print("********", actual)

        time.sleep(2)