from selenium.common.exceptions import NoSuchElementException
from makePromo import init
from userdata import login, password, amount_keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    driver = webdriver.Chrome()
    driver.get('https://funline.pw/lk/')
    logIn(driver)
    time.sleep(3)
    pasteKeys(driver)
    time.sleep(2000)


def logIn(self):
    loginField = self.find_element_by_css_selector("input[name='username'][type='text']")
    passField = self.find_element_by_css_selector("input[name='password'][type='password']")
    loginField.send_keys(login)
    passField.send_keys(password)
    self.find_element_by_css_selector("input[name='remember'][type='checkbox']").click()

    # findPicture(self)
    time.sleep(3)
    da = False
    while not da:
        try:
            findPicture(self)
            time.sleep(5)
            print(self.find_element_by_class_name("captcha-modal__icons-title").text)
            if self.find_element_by_class_name("captcha-modal__icons-title").text == "Отлично!":
                da = True
                self.find_element_by_css_selector("input[type='submit']").click()
        except NoSuchElementException:
            print('Not found')


def findPicture(self):
    self.find_elements_by_class_name("captcha-image")[2].click()


def pasteKeys(self):
    list = init()
    print(list)
    passedKeys = amount_keys

    for i in list:
        field = self.find_element_by_css_selector("input[name='promo_code']")
        field.send_keys(i)
        self.find_element_by_class_name("btn-inverse").click()
        time.sleep(0.5)
        try:
            if self.find_element_by_class_name("alert-error").text.replace("\n", "") == "×Ошибка! Промо код не найден, проверьте правильность ввода":
                passedKeys = passedKeys - 1
        except NoSuchElementException:
            pass

    print("Успешных кодов: ", passedKeys)

if __name__ == '__main__':
    main()
