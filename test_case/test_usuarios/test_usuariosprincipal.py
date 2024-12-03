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
        print("Paso prueba")
        time.sleep(2)

    def test_iniciar_con_metodo_externo(self):
        # Aquí usamos el metodo importado
        insertar_usuario_contrasena(self.driver)
    
    def test_desplegar_usuarios(self):
        insertar_usuario_contrasena(self.driver)
        self.driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Usuarios')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='nav-link']//p[contains(text(),'Listado de usuarios')]").click()
        time.sleep(2)
