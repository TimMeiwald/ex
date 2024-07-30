from selenium import webdriver
from os import getcwd
from os.path import join


class OptionsConstructor():
    def __init__(self):
        self.options = webdriver.FirefoxOptions()
    def get_options(self):
        return self.options
class ServiceConstructor():
    def __init__(self):
        executable_path = join(getcwd(), "drivers", "geckodriver.exe")
        self.service = webdriver.FirefoxService(executable_path=str(executable_path))
    def get_service(self):
        return self.service

class DriverConstructor():
    def __init__(self):
        self.options = OptionsConstructor().get_options()
        self.service = ServiceConstructor().get_service()
    def get_driver(self):
        return webdriver.Firefox(service = self.service, options= self.options)    