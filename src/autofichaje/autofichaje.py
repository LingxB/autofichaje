from selenium import webdriver
from src.utils.file_utils import load_envar, get_envar
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


class AutoFichaje(object):

    def __init__(self):
        load_envar()
        self.input_nie = get_envar('USER_NIE')
        self.input_password = get_envar('USER_PASSWORD')
        self.url = get_envar('A3HRGO_URL')
        self.driver = webdriver.Chrome(get_envar('DRIVER_PATH'))
        self.driver.get(self.url)

    def login(self):
        _nie = self.driver.find_element_by_id("Login")
        _nie.send_keys(self.input_nie)
        _password = self.driver.find_element_by_id("Password")
        _password.send_keys(self.input_password)
        self.driver.find_element_by_class_name("btnLogin").click()

    def mark(self):
        self.driver.find_element_by_link_text("Mis Fichajes").click()
        self.driver.find_element_by_xpath(""".//span[@class = "fa fa-clock-o iconoAyuda"]""").click()
        self.driver.find_element_by_id('btnGuardar').click()

    def get_status(self, timeout=10):

        t = 0
        while t < timeout:
            try:
                self.driver.find_element_by_link_text("Mis Fichajes").click()
                break
            except NoSuchElementException:
                time.sleep(1)
                t += 1

        last_action = self.driver.find_element_by_xpath(
            "//table[@class='table-striped  table-hover col-lg-12 col-md-12 col-sm-12 col-xs-12']"
            "/tbody[2]/tr/td[2]"
        ).text
        last_timestamp = self.driver.find_element_by_xpath(
            "//table[@class='table-striped  table-hover col-lg-12 col-md-12 col-sm-12 col-xs-12']"
            "/tbody[2]/tr/td[3]"
        ).text
        last_timestamp = datetime.strptime(last_timestamp, "%d/%m/%Y %H:%M:%S")
        return last_action, last_timestamp
