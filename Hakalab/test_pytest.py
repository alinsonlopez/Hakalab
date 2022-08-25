import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Pages.page_elements import Test_Elements as Elements


@pytest.fixture(scope='module')
def setup_startsandends():
    print("iniciando test...")
    yield
    print(" ...fin de test")


def setup_function(function):

    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def teardown_function(function):

    driver.close()


@pytest.mark.elementos
def test_elementos(setup_startsandends):

    Elements(driver).inputs()


@pytest.mark.psimple
def test_psimple(setup_startsandends):
    a = 0
    b = 1
    assert False, "elemento con error"

# Para ver a detalle ejecutar:
# pytest /home/alinson/proyectoSelenium/Hakalab/test_pytest.py -s -v -m elementos
