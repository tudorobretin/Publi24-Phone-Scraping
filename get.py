from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class Get:
    def __init__(self):
        self.init = 0


    def article_links(self):
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
        print(number_of_pages)
        links = []

        for page in range(1, number_of_pages - 1):
            #time.sleep(1)
            print(page)
            article_titles = driver.find_elements(By.CSS_SELECTOR, '.article-title a')
            for title in article_titles:
                link = title.get_attribute('href')
                links.append(link)
            next_page = driver.find_elements(By.CLASS_NAME, 'arrow')[1]
            next_page.click()

        return links

    def phone_numbers(self):
        pass



