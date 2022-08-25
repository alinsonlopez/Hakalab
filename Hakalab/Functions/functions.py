import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class Functions:

    def __init__(self, driver):
        self.driver = driver
        pass

    # Abre url y maximiza la ventana
    def open_url(self, url, delay=0):
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        print(f"Pagina abierta: {url}")
        time.sleep(delay)

    # Busca el elemento por medio de xpath

    def search_for_xpath(self, xpath):
        driver = self.driver
        try:
            element = (WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, xpath))))
            return element
        except TimeoutException as ex:
            print(f"elemento no encontrado - XPATH:{xpath}")

    # Envia texto por medio de xpath validando si existe el elemento

    def send_for_xpath(self, xpath, value, delay=0):
        driver = self.driver
        try:
            element = Functions(driver).search_for_xpath(xpath)
            element.send_keys(value)
            print(f"Escribiendo {value}")
            time.sleep(delay)
        except Exception:
            print(
                f"Error: El elemento {value} no fue enviado, intente corregir xpath")

    # Hace click

    def click_for_xpath(self, xpath, delay=0):
        driver = self.driver
        try:
            element = Functions(driver).search_for_xpath(xpath)
            element.click()
            time.sleep(delay)
            print(f"{element.get_attribute('id')} clickeado")
        except Exception:
            print(
                f"El elemento {element.get_attribute('id')} no fue clickeado")

    # Selecciona por valor
    def selects_for_value(self, xpath, value, delay=0):
        driver = self.driver
        try:
            element = Functions(driver).search_for_xpath(xpath)
            Select(element).select_by_value(value)
            print(f"elemento {value} seleccionado")
            time.sleep(delay)
        except Exception:
            print(
                f"Error: elemento {value} no fue seleccionado en {element.get_attribute('id')} ")

    # Selecciona por index, puede seleccionar varios
    def selects_for_index(self, xpath, delay=0, *index):
        driver = self.driver
        for i in index:
            try:
                element = Functions(driver).search_for_xpath(xpath)
                Select(element).select_by_index(i)
                print(f"elemento {i} seleccionado")
                time.sleep(delay)
            except Exception:
                print(
                    f"Error: index {i} no fue seleccionado en {element.get_attribute('id')}, es posible que no exista")

    # Varias Acciones de mouse
    def actions_mouse(self, xpath: str, action: int, delay=0):
        """
        Funcion para accion del mouse.

        Args:
            xpath: xpath.
            action: accion a realizar 0 - click / 1 - Dclick / 2 - CDerecho
            delay: tiempo de retraso, por defecto es 0.

        Returns:
            Evento de mouse.
        """
        try:
            driver = self.driver
            element = Functions(driver).search_for_xpath(xpath)
            if action == 0:
                ActionChains(driver).click(element).perform()
                time.sleep(delay)
                print(f"{element.get_attribute('id')} clickeado")
            elif action == 1:
                ActionChains(driver).double_click(element).perform()
                time.sleep(delay)
                print(f"{element.get_attribute('id')} doble clickeado")
            elif action == 2:
                ActionChains(driver).context_click(element).perform()
                time.sleep(delay)
                print(f"{element.get_attribute('id')} clickeado con boton derecho")
            else:
                print(
                    f"Error: elemento {element.get_attribute('id')} no fue clickeado ya que la accion {action} no esta permitida")
        except Exception:
            print(
                f"Error: elemento {element.get_attribute('id')} no fue clickeado")

    # Mover barra horizontal
    def drag_mouse(self, xpath, x, y, delay=0):
        try:
            driver = self.driver
            element = Functions(driver).search_for_xpath(xpath)
            ActionChains(driver).drag_and_drop_by_offset(
                element, x, y).release().perform()
            print(f"elemento {element.get_attribute('id')} ha sido movido")
            time.sleep(delay)
        except Exception:
            print(
                f"Error: elemento {element.get_attribute('id')} no ha sido movido")
