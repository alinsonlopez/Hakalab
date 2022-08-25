import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Pages.page_elements import Test_Elements as Elements


class InputFormsCheck(unittest.TestCase):

    # Abri Navegador.
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))

    def test_elementos(self):
        driver = self.driver
        Elements(driver).inputs()
        Elements(driver).selectores()
        Elements(driver).checkbox()
        Elements(driver).botones()
        # Debe cambiar nombre de usuario del pc para que funcione
        Elements(driver).subir_descargar()

        print("Prueba finalizada")

    def tearDown(self):
        self.driver.close()


# This line sets the variable “__name__” to have a value “__main__”.
# If this file is being imported from another module then “__name__” will be set to the other module's name.
if __name__ == "__main__":
    unittest.main()
