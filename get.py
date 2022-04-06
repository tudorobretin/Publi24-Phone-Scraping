from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import base64
import os
from ocr import OCR


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
        # number_of_pages - 1
        for page in range(1, 2):
            #time.sleep(1)
            print(page)
            article_titles = driver.find_elements(By.CSS_SELECTOR, '.article-title a')
            for title in article_titles:
                link = title.get_attribute('href')
                links.append(link)
            next_page = driver.find_elements(By.CLASS_NAME, 'arrow')[1]
            next_page.click()

        return links

    def phone_numbers(self, article_links):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\MAXMEDIA\\Desktop\\Python downloads\\Chromedriver\\chromedriver.exe")
        URL = "https://www.publi24.ro/anunturi/matrimoniale/"
        driver.get(URL)

        over_18_accept = driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div/a[2]')
        over_18_accept.click()

        accept_cookies = driver.find_element(By.XPATH, '/html/body/div[17]/div/div/a[1]')
        accept_cookies.click()

        ocr = OCR()
        phone_numbers_list = []
        for link in article_links:
            #time.sleep(1)
            driver.get(link)

            try:
                show_number = driver.find_element(By.XPATH, '/html/body/div[15]/div/div/div[4]/div[1]/div[1]/form/button')
                show_number.click()
                time.sleep(0.3)

                number_encoded_raw = driver.find_element(By.XPATH,
                                                         '/html/body/div[15]/div/div/div[4]/div[1]/div[1]/form/button/span')
                number_encoded = number_encoded_raw.get_attribute("style").split(",")[1].split('"')[0]
                # print(number_encoded_raw.get_attribute("style").split(",")[1].split('"')[0])
                phone_number = ocr.image_to_text(encoded_image=number_encoded)
                print(phone_number)
                if len(phone_number) == 10 and phone_number[0]=="0":
                    phone_numbers_list.append(phone_number)
                else:
                    phone_numbers_list.append("EXCEPT")

            except:

                print("entered except")
                pass

        return phone_numbers_list




