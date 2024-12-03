from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#importo el metodo que esta dentro del archivo sesion.py 
from test_case.sesion import insertar_usuario_contrasena
import time

class TestRoles:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost/Ventas/login/')
    
    def teardown_method(self):
        self.driver.quit()
        print("  Paso prueba")
    
    def test_desplegar_roles(self):
        #importamos la clase de sesion.py
        insertar_usuario_contrasena(self.driver)
        #Desplegamos el menu del boton roles
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Roles')]").click()
        time.sleep(1)
        #seleccionamos el boton Listado de roles 
        self.driver.find_element(By.XPATH, "//a[@class='nav-link']//p[contains(text(),'Listado de roles')]").click()
        time.sleep(1)
        # Verifica  que el contenido este ahi lista roles
        actual = self.driver.find_element(By.XPATH, "//div[contains(@class,'container-fluid')]//h1").text
        esperado = "Listado de roles"
        print("********", actual)
        assert esperado in actual, f"Error. Actual: {actual}, Esperado: {esperado}"
        time.sleep(2)

        #volvemos a desplegar el boton de roles y seleccionamos el boton creart roles
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Roles')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@class='nav-link']//p[contains(text(),'Creación de rol')]").click()
        actual = self.driver.find_element(By.XPATH, "//div[contains(@class,'container-fluid')]//h1").text
        esperado = "Registro de un Rol"
        print("********", actual)
        assert esperado in actual, f"Error. Actual: {actual}, Esperado: {esperado}"
        time.sleep(2)
    
    #############################################
    ############# MOVER ESTE METODO A OTRA CLASE 
    ############# EN OTRO ARCHIVO .PY
    def test_crear_rol(self):
        #importamos la clase
        insertar_usuario_contrasena(self.driver)
         #volvemos a desplegar el boton de roles y seleccionamos el boton creart roles
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Roles')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@class='nav-link']//p[contains(text(),'Creación de rol')]").click()
        time.sleep(1)
        #Insertamos el nombre del usuario que desemos crear
        #self.driver.find_element(By.XPATH, "//input[@name='rol']").send_keys("Pachirisu")
        #time.sleep(1)
        #click al boton guardar
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        time.sleep(2)
        ###################################
        ########PRUEBA#######
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Roles')]").click()
        time.sleep(1)
        #seleccionamos el boton Listado de roles 
        self.driver.find_element(By.XPATH, "//a[@class='nav-link']//p[contains(text(),'Listado de roles')]").click()
        ####################################
        actual = self.driver.find_element(By.XPATH, "//tr[contains(@class,'odd')]//td[contains(text(),'ADMINISTRADOR')]").text
        esperada = "ADMINISTRADOR"
        print("********", actual)
        assert esperada in actual, f"Error. Actual: {actual}, Esperado: {esperada}"
        time.sleep(2)
        
        ####### HACER CLICK AL BOTON EDITAR #######
        self.driver.find_element(By.XPATH, "//tr[contains(@class,'even')]//div[@class='btn-group']//a[@class='btn btn-success']").click()
        time.sleep(2)

        ############## el locator de los botones es correcto pero intercala entre even y odd si tenemos 3 seran odd
        ############## even, odd trabajar el editar, ver y eliminar con la loactor de una sola clase osea un even o un odd
        ############## para no tener conflictos copn los locators