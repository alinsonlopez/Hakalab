from Functions.functions import Functions

# Probar Pagina Elementos


class Test_Elements:

    def __init__(self, driver):
        self.driver = driver
        pass

    def open(self):  # Valida si es la pagina correcta o la abre
        f = Functions(self.driver)
        if self.driver.title != "HakaTools":
            f.open_url("https://www.hakalab.com/hakatools/elements")

    def inputs(self):
        # Valida pagina
        Test_Elements(self.driver).open()

        # Acorta la llamada a la Functions
        f = Functions(self.driver)

        # Clickear Inputs
        f.click_for_xpath("//a[@id='list-inputs-list']")

        # XPath
        name = "//input[contains(@id,'InputUserName')]"
        email = "//input[contains(@id,'email')]"
        password = "//input[contains(@id,'password')]"
        textarea = "//textarea[contains(@id,'exampleFormControlTextarea1')]"
        search = "//input[contains(@id,'search')]"
        url = "//input[contains(@id,'url')]"
        phone = "//input[contains(@id,'tel')]"
        number_type = "//input[contains(@id,'number')]"
        custom_range = "//input[@id='customRange1']"
        date = "//input[@id='date']"
        month = "//input[@id='month']"
        week = "//input[@id='week']"
        hour = "//input[@id='time']"
        datetime = "//input[@id='datetime-local']"
        color = "//input[@id='color']"

        f.send_for_xpath(name, "Alinson", .5)
        f.send_for_xpath(email, "alinsonl11@gmail.com", .5)
        f.send_for_xpath(password, "almanail", .5)
        f.send_for_xpath(
            textarea, "Tecnico informatico apasionado por la tecnologia", .5)
        f.send_for_xpath(search, "Como formar parte de Hakalab?", .5)
        f.send_for_xpath(url, "https://www.linkedin.com/in/alinsonlopez/", .5)
        f.send_for_xpath(phone, "934805187", .5)
        f.send_for_xpath(number_type, "29", .5)
        f.drag_mouse(custom_range, 80, 0, 2)

    def selectores(self):
        # Valida pagina
        Test_Elements(self.driver).open()

        # Acorta la llamada a la Functions
        f = Functions(self.driver)

        # Clickear Selectores
        f.click_for_xpath("//a[@id='list-selects-list']")

        # XPath
        languaje = "//select[@id='selectorLenguaje']"
        fruits = "//select[@id='selectMultiplefrutas']"

        f.selects_for_value(languaje, "phyton", .5)
        f.selects_for_index(fruits, 1, 0, 1, 2)

    def selector_de_fechas(self):
        # Valida pagina
        Test_Elements(self.driver).open()

        # Acorta la llamada a la Functions
        f = Functions(self.driver)

        # Clickear Selectores de Fecha
        f.click_for_xpath("//a[@id='list-pickers-list']")

    def checkbox(self):
        # Valida pagina
        Test_Elements(self.driver).open()

        # Acorta la llamada a la Functions
        f = Functions(self.driver)

        # Clickear Checkbox
        f.click_for_xpath("//a[@id='list-checkbox-list']")

        # XPath
        simple = "//input[@id='simpleCheckbox']"

        f.click_for_xpath(simple, 2)

    def botones(self):

        # Valida pagina
        Test_Elements(self.driver).open()

        # Acorta la llamada a la Functions
        f = Functions(self.driver)

        # Clickear Botones
        f.click_for_xpath("//a[@id='list-buttons-list']")

        # XPath
        single_click = "//button[@id='singleClickButton']"
        double_click = "//button[@id='DoubleClickButton']"
        rigth_click = "//button[@id='ClickDerechoButton']"

        f.actions_mouse(single_click, 0, .5)
        f.actions_mouse(double_click, 1, .5)
        f.actions_mouse(rigth_click, 2, 2)

    def subir_descargar(self):
        # Valida pagina
        Test_Elements(self.driver).open()

        # Acorta la llamada a la Functions
        f = Functions(self.driver)

        # Clickear Subir y Descargar Archivo
        f.click_for_xpath("//a[@id='list-upload-list']")

        # XPath
        upload = "//input[@id='uploadFileInput']"
        download = "//a[@id='downloadButton']"

        f.click_for_xpath(download, 2)
        f.send_for_xpath(upload, "//home/alinson/Downloads/Gorrion..jpeg", 2)
