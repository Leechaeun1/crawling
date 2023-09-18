from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import os

chrome_options = Options()
chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(options=chrome_options)

search_terms = ['강아지', '고양이', '얼룩말']

download_path = r'C:\Users\hs9hs\크롤링' 
os.makedirs(download_path, exist_ok=True)

for search_term in search_terms:
    URL = f'https://www.google.co.kr/imghp?q={search_term}'
    driver.get(url=URL)

    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
    search_box.send_keys(Keys.RETURN)

    image_results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.islrc .islir img')))

    num_images_to_save = 11  # 이미지 저장 개수

    for index, image in enumerate(image_results[:num_images_to_save], start=1):
        image_url = image.get_attribute('src')
        file_name = f'{search_term.replace(" ", "_")}_image_{index}.jpg' 
        file_path = os.path.join(download_path, file_name)

        try:
            urllib.request.urlretrieve(image_url, file_path)
            print(f"Image {index} for '{search_term}' downloaded to: {file_path}")
        except Exception as e:
            print(f"An error occurred while downloading image {index} for '{search_term}': {e}")

driver.quit()
