
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(executable_path=r'C:/chromedriver/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def login():
    # Вводим email
    pytest.driver.find_element(By.ID, "email").send_keys('igobedasvili@gmail.com')
    # Вводим пароль
    pytest.driver.find_element(By.ID, "pass").send_keys('mama020160_B')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

def test_check_pet_cards():
    login()

    assert WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-deck .card-img-top')))
    assert WebDriverWait(pytest.driver, 1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-deck .card-title')))
    assert WebDriverWait(pytest.driver, 1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-deck .card-text')))

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
       assert images[i].get_attribute('src') != ''
       assert names[i].text != ''
       assert descriptions[i].text != ''
       assert ', ' in descriptions[i]
       parts = descriptions[i].text.split(", ")
       assert len(parts[0]) > 0
       assert len(parts[1]) > 0
