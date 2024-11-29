from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración de capacidades deseadas
desired_caps = {
    "platformName": "Android",                # Cambia a "iOS" si pruebas en iPhone
    "platformVersion": "10",                 # Versión de Android o iOS
    "deviceName": "emulator-5554",           # Nombre del dispositivo
    "automationName": "UiAutomator2",        # Motor de automatización
    "app": "/ruta/a/tu_aplicacion.apk",      # Ruta del archivo APK
    "appPackage": "com.example.tuapp",       # Paquete de la app
    "appActivity": "com.example.MainActivity" # Actividad principal
}

#sdsadsadsadsa
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

try:
    
    wait = WebDriverWait(driver, 10)
    boton_iniciar_sesion = wait.until(EC.presence_of_element_located((By.ID, "btnLogin")))

    
    boton_iniciar_sesion.click()

    print("Se hizo clic en el botón INICIAR SESIÓN correctamente.")

finally:
 
    driver.quit()
