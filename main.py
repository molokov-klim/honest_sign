import time
import tkinter as tk
from tkinter import simpledialog

import pyautogui
from icecream import ic
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound
from PIL import Image

# Путь к аудиофайлу (может быть абсолютным или относительным)
sound_file = 'sound.mp3'

# Создаем экземпляр веб-драйвера
chrome_options = Options()
chrome_options.add_extension('CryptoPro.crx')
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(options=chrome_options)
rutoken_modal = ("rutoken_modal.png"
                 "")


def done():
    print(
        "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(
        "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(
        "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    input('done')



def wait_for_modal(timeout: int = 30) -> bool:
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            # Пытаемся найти изображение на экране
            location = pyautogui.locateOnScreen(rutoken_modal, confidence=0.8)
            if location:
                print("Модальное окно появилось!")
                return True
        except pyautogui.ImageNotFoundException:
            # Если не найдено, продолжаем ожидание
            pass
        time.sleep(0.5)  # Ждем полсекунды перед следующей проверкой

    print("Тайм-аут: модальное окно не появилось.")
    return False  # Возвращаем False, если модальное окно не появилось


def wait_for_modal_disappear(timeout: int = 10) -> bool:
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateOnScreen(rutoken_modal, confidence=0.8)
            if location is None:
                print("Модальное окно исчезло!")
                return True
        except pyautogui.ImageNotFoundException:
            return True  # Модальное окно считается исчезнувшим

        time.sleep(0.5)  # Ждем полсекунды перед следующей проверкой

    print("Тайм-аут: модальное окно не исчезло.")
    return False  # Возвращаем False, если модальное окно не исчезло


def accept_rutoken():
    start_time = time.time()
    while time.time() - start_time < timeout_wait:
        wait_for_modal()
        pyautogui.press('left')
        pyautogui.press('enter')
        wait_for_modal_disappear()
        if wait_for_modal_disappear():
            return


try:
    # Открываем веб-страницу
    driver.get("https://markirovka.crpt.ru/login-kep")  # Замени URL на тот, который нужен
    timeout_wait = 90

    # Окно во весь экран
    driver.maximize_window()

    WebDriverWait(driver, timeout_wait).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/button'))
    ).click()

    # Выбор опции из системного окна с помощью pyautogui
    accept_rutoken()

    # Клик на элемент, чтобы перейти к следующему шагу
    WebDriverWait(driver, timeout_wait).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div/h5'))
    ).click()

    # Выбор опции из системного окна с помощью pyautogui
    accept_rutoken()

    # Клик на элемент для перехода к следующему шагу
    WebDriverWait(driver, timeout_wait).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div[24]/div'))
    ).click()

    # Клик на кнопку для открытия выпадающего списка
    WebDriverWait(driver, timeout_wait).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.jss157 > div > button'))
    ).click()

    # Клик на кнопку в заголовке окна
    WebDriverWait(driver, timeout_wait).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    '#WindowHeader > div > div.MuiStack-root.css-1xoglta > div.MuiBox-root.css-k008qs > div > div > div > div > a:nth-child(3)'))
    ).click()

    while True:
        time.sleep(10)
        ic()

        # Клик на кнопку в заголовке окна
        WebDriverWait(driver, timeout_wait).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '#WindowHeader > div:nth-child(2) > div.MuiStack-root.css-9rn2kd > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeLarge.MuiButton-containedSizeLarge.MuiButton-disableElevation.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeLarge.MuiButton-containedSizeLarge.MuiButton-disableElevation.css-sud0j'))
        ).click()

        # Клик на элемент в выпадающем меню
        WebDriverWait(driver, timeout_wait).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-1q80h7n > a:nth-child(6) > div > span'))
        ).click()

        # Выбор опции из системного окна с помощью pyautogui
        accept_rutoken()

        # Клик на кнопку для перехода к следующему шагу
        WebDriverWait(driver, timeout_wait).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '#WindowHeader > div:nth-child(2) > div.MuiBox-root.css-ximfwq > div.MuiStack-root.css-shayf4 > button:nth-child(2)'))
        ).click()

        # Фильтр
        WebDriverWait(driver, timeout_wait).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id=\"WindowHeader\"]/div[3]/div/div/div[2]/div/button[2]"))
        ).click()

        # Нанесен чекбокс
        WebDriverWait(driver, timeout_wait).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "body > div.MuiDrawer-root.MuiDrawer-modal.MuiModal-root.css-hddgwj > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-elevation16.MuiDrawer-paper.MuiDrawer-paperAnchorRight.css-crd5i7 > div > form > div.FilterForm-ScrollArea.MuiBox-root.css-0 > div.FilterForm-FilterList.MuiBox-root.css-0 > div:nth-child(3) > div.MuiStack-root.css-sg6wi7 > label:nth-child(3) > span.MuiButtonBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.PrivateSwitchBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.css-1mq01r"))
        ).click()

        time.sleep(5)

        # Применить
        WebDriverWait(driver, timeout_wait).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "body > div.MuiDrawer-root.MuiDrawer-modal.MuiModal-root.css-hddgwj > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-elevation16.MuiDrawer-paper.MuiDrawer-paperAnchorRight.css-crd5i7 > div > form > div.FilterForm-Footer.MuiBox-root.css-0 > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeLarge.MuiButton-containedSizeLarge.MuiButton-disableElevation.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeLarge.MuiButton-containedSizeLarge.MuiButton-disableElevation.css-sud0j"))
        ).click()

        WebDriverWait(driver, timeout_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '#redesign-portal > div.MuiBox-root.css-178yklu > div.MuiBox-root.css-75a7np > div:nth-child(1) > div > div.ReactVirtualized__Grid.ReactVirtualized__List > div > div:nth-child(1) > div > div.MuiTableCell-root.MuiTableCell-sizeMedium.DataCell.ToggleCell.MuiBox-root.css-1fy480w > div > span'))
        ).click()

        # Клик на кнопку для подтверждения
        WebDriverWait(driver, timeout_wait).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '#redesign-portal > div.MuiBox-root.css-0 > div > div > div > div > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeLarge.MuiButton-containedSizeLarge.MuiButton-disableElevation.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeLarge.MuiButton-containedSizeLarge.MuiButton-disableElevation.css-sud0j'))
        ).click()

        driver.find_element(By.CSS_SELECTOR,
                            'div.MuiSelect-select.MuiSelect-standard.MuiInputBase-input.MuiInput-input.css-1cccqvr').click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[text()='Испорчено либо утеряно СИ с КМ']").click()

        # Прокрутка страницы вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ожидание, пока страница прокрутится и элементы появятся
        WebDriverWait(driver, timeout_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.MuiAutocomplete-input'))
        )
        elements = driver.find_elements(By.CSS_SELECTOR, 'input.MuiAutocomplete-input')
        input_element = elements[-1]
        input_element.click()
        input_element.send_keys("6104630000")

        # Подождите, пока появится список
        dropdown_list = WebDriverWait(driver, timeout_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul[role="listbox"]'))
        )

        # Найдите первый элемент в выпадающем меню
        first_option = WebDriverWait(dropdown_list, timeout_wait).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li:first-child'))
        )

        # Кликните на первый элемент
        first_option.click()

        # Клик на чекбокс
        driver.find_element(By.XPATH, '//*[@id="WindowHeader"]/div[2]/div[3]/div/div[2]/div[1]/label/span[1]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Первичный документ')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Разрешительный документ')]").click()
        time.sleep(1)

        # Прокрутка страницы вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        elements = driver.find_elements(By.CSS_SELECTOR,
                                        "div.MuiSelect-select.MuiSelect-standard.MuiInputBase-input.MuiInput-input")

        input_element = elements[-1]
        input_element.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[contains(text(), 'Декларация о соответствии')]").click()
        time.sleep(1)

        elements = driver.find_elements(By.CSS_SELECTOR,
                                        "div.MuiSelect-select.MuiSelect-standard.MuiInputBase-input.MuiInput-input")

        input_element = elements[-2]
        input_element.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[contains(text(), 'Товарная накладная')]").click()
        time.sleep(1)
        number_first_doc = driver.find_element(By.XPATH,
                                               "//div[@class='MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root css-qjn9kc']//div[@class='MuiInputBase-root MuiInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl css-154zzzm']//input[@name='products.0.primaryDocumentNumber']")
        number_first_doc.click()
        number_first_doc.send_keys("24/08/2023")
        time.sleep(1)
        name_first_doc = driver.find_element(By.XPATH,
                                             "//div[@class='MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root css-qjn9kc']//div[@class='MuiInputBase-root MuiInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl css-154zzzm']//input[@name='products.0.primaryDocumentCustomName']")
        name_first_doc.click()
        name_first_doc.send_keys("Приложение к Договору поставки")
        time.sleep(1)
        date_first_doc = driver.find_element(By.XPATH,
                                             "//div[@class='MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root css-fyenpg']//div[@class='MuiInputBase-root MuiInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-adornedEnd css-154zzzm']//input[@name='products.0.primaryDocumentDate']")
        date_first_doc.click()
        date_first_doc.send_keys("24.08.2023" + Keys.ENTER)
        time.sleep(1)
        ds_number = driver.find_element(By.XPATH,
                                        "//div[@class='MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root css-qjn9kc']//div[@class='MuiInputBase-root MuiInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl css-154zzzm']//input[@name='products.0.certificateDocumentData.0.certificateNumber' and @required='']")
        ds_number.click()
        ds_number.send_keys("ЕАЭС N RU Д-CN.РА02.В.94889/24")
        date_ds = driver.find_element(By.XPATH,
                                      '//input[@name="products.0.certificateDocumentData.0.certificateDate" and @type="text"]')
        date_ds.click()
        time.sleep(1)
        date_ds.send_keys("21.05.2024" + Keys.ENTER)
        time.sleep(1)
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-containedPrimary[type="submit"]')
        submit_button.click()

except Exception as e:
    print(f"Ошибка: {e}")
    with open('source.html', 'w') as file:
        file.write(driver.page_source)


finally:
    # Закрываем браузер
    driver.quit()

# ЕАЭС N RU Д-CN.РА02.В.94889/24 от 21.05.2024 действует до 20.05.2027
