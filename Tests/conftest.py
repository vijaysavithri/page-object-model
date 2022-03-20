from selenium import webdriver
#from webdriver_manager.chrome import chromeDriverManager
import pytest

@pytest.fixture(params=["Chrome"],scope='class')
def init_driver(request):
    print("------setup------------")
    if request.param=="Chrome":
        web_driver=webdriver.Chrome()
    if request.param=="Firfox":
        web_driver=webdriver.Firefox()
    request.cls.driver=web_driver
    yield
    print("----------tear down----------")
    web_driver.close()
