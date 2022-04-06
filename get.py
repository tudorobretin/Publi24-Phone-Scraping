from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class Get:
    def __init__(self):
        self.init = 0


    def article_links(self):

        def get_number_of_pages():
            driver = webdriver.Chrome(
                executable_path="C:\\Users\\MAXMEDIA\\Desktop\\Python downloads\\Chromedriver\\chromedriver.exe")
            URL = "https://www.publi24.ro/anunturi/matrimoniale/"
            driver.get(URL)
            time.sleep(1)

            over_18_accept = driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div/a[2]')
            over_18_accept.click()

            accept_cookies = driver.find_element(By.XPATH, '/html/body/div[17]/div/div/a[1]')
            accept_cookies.click()

            results_per_page = driver.find_element(By.XPATH, '/html/body/div[11]/div/div/div[4]/ul[1]/li[1]/p/span[2]')
            results_per_page.click()

            number_of_pages = int(driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div[4]/ul[2]/li[11]/a').text)
            return number_of_pages

        pages = get_number_of_pages()
        print(pages)

        time.sleep(100)

    def phone_numbers(self):
        pass



