from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

options = Options()
options.headless = False
# options.add_argument('window-size=1920x1080')

web = "https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=8a113f1a-dc38-418d-b671-3cca04245da5&pf_rd_r=B2S0T9ACNZNTS4BRF26A&pageLoadId=LGzChPKuzMRIStRw&creativeId=1642b4d1-12f3-4375-98fa-4938afc1cedc"
path = "C:/Users/alper/AlperProjects/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

pagination = driver.find_element_by_xpath(
    '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements_by_tag_name('li')
last_page = int(pages[-2].text)

book_title = []
book_author = []
book_length = []
current_page = 1

while current_page <= last_page:
    # Implicit Wait
    time.sleep(2)
    # Explicit Wait
    # container = driver.find_element_by_class_name('adbl-impression-container ')
    container = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container ')))
    # products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')
    products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located(
        (By.XPATH, './/li[contains(@class, "productListItem")]')))

    for product in products:
        book_title.append(product.find_element_by_xpath(
            './/h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element_by_xpath(
            './/li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element_by_xpath(
            './/li[contains(@class, "runtimeLabel")]').text)

    current_page = current_page + 1
    try:
        next_page = driver.find_element_by_xpath(
            './/span[contains(@class , "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()

df_books = pd.DataFrame(
    {'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books_pagination.csv', index=False)
