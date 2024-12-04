from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#importo el metodo que esta dentro del archivo sesion.py 
from test_case.sesion import insertar_usuario_contrasena
import time

class TestUsuarios:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost/Ventas/login/')
    
    def teardown_method(self):
        self.driver.quit()
        print("  Paso prueba")
        

    #def test_iniciar_con_metodo_externo(self):
        # Aquí usamos el metodo importado
        #insertar_usuario_contrasena(self.driver)
    
    def test_desplegar_usuarios(self):
        insertar_usuario_contrasena(self.driver)
        #desplegamos el boton usuarios
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Usuarios')]").click()
        time.sleep(1)
        #hacemos click en el boton listado de usuarios
        self.driver.find_element(By.XPATH, "//a[@class='nav-link']//p[contains(text(),'Listado de usuarios')]").click()
        time.sleep(1)
        # Verifica que el contenido esperado esté ahi Listado usuario
        actual = self.driver.find_element(By.XPATH, "//div[contains(@class,'container-fluid')]//h1").text
        esperada = "Listado de usuario"
        print("********", actual)
        assert esperada in actual, f"Error. Actual: {actual}, Esperado: {esperada}"
        time.sleep(2)
    
    
        #volvemos a desplegar el menu
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Usuarios')]").click()
        time.sleep(1)
        #hacemos click en el boton creacion de usuario
        self.driver.find_element(By.XPATH,"//a[@class='nav-link']//p[contains(text(),'Creación de usuario')]").click()
        time.sleep(1)
        #Verifica que el contenido esperado esté ahi creacion de usuario
        actual = self.driver.find_element(By.XPATH, "//div[contains(@class,'col-sm-12')]//h1").text
        esperada = "Registro de un nuevo usuario"
        print("********", actual)
        assert esperada in actual, f"Error. Actual: {actual}, Esperado: {esperada}"
        time.sleep(2)
    
    def test_crear_usuario(self):
        #Pruebas visuales completas procedemos a crear un usuario
        ########################################################
        ############## EN OTRA CLASE CREAMOS EL USUARIO#########
        insertar_usuario_contrasena(self.driver)
        #desplegamos el boton usuarios
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Usuarios')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//a[@class='nav-link']//p[contains(text(),'Creación de usuario')]").click()
        time.sleep(1)
        #creacion de un usuario
        #self.driver.find_element(By.XPATH, "//input[@name='nombres']").send_keys("Maluma")
        #self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("maluma@gmail.com")
        #self.driver.find_element(By.XPATH, "//select[@name='rol']//option[@value='3']").click()
        #self.driver.find_element(By.XPATH, "//input[@name='password_user']").send_keys("maluma@123")
        #self.driver.find_element(By.XPATH, "//input[@name='password_repeat']").send_keys("maluma@123")
        #self.driver.find_element(By.XPATH, "//div[contains(@class,'form-group')]//button[@class='btn btn-primary']").click()
        #time.sleep(3)
        #volvemos a la lista de usuario para ver el nuevo usuario añadido
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Usuarios')]").click()
        time.sleep(1)
        #hacemos click en el boton listado de usuarios para verificar que el usuario este creado
        self.driver.find_element(By.XPATH, "//a[@class='nav-link']//p[contains(text(),'Listado de usuarios')]").click()
        #buscamos el usuario creado en la lista y verificamos
        actual = self.driver.find_element(By.XPATH, "//tr[@class='odd']//td[contains(text(),'maluma@gmail.com')]").text
        esperada = "maluma@gmail.com"
        print("********", actual)
        assert esperada in actual, f"Error. Actual: {actual}, Esperado: {esperada}"
        
        #//tr[contains(@class,'odd')]//td[text()='maluma@gmail.com']//a[@class,'btn btn-info']
        time.sleep(2)