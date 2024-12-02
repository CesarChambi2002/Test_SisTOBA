from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14"
options.device_name = "R5CT303H0VA"
options.automation_name = "UiAutomator2"
options.app = r"C:\Users\conra\AdministradorTOBA\app\build\outputs\apk\debug\app-debug.apk"
options.app_package = "com.example.administradortoba"
options.app_activity = "com.example.administradortoba.LoginActivity"
options.uiautomator2_server_install_timeout = 60000  


driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723", 
    options=options
)

try:
  
    wait = WebDriverWait(driver, 10)
    
    
    campo_email = wait.until(EC.presence_of_element_located((By.ID, "edtUsuario")))
    campo_email.send_keys("grover@gmail.com")  

    
    campo_password = wait.until(EC.presence_of_element_located((By.ID, "edtPassword")))
    campo_password.send_keys("12345678")  

  
    boton_iniciar_sesion = wait.until(EC.presence_of_element_located((By.ID, "btnLogin")))
    boton_iniciar_sesion.click()

    print("Correcto")

finally:
  
    driver.quit()
