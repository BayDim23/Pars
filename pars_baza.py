import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

link = "https://www.divan.ru/category/podushki"  # Убедитесь, что URL указан правильно

driver.get(link)

time.sleep(5)

podushki = driver.find_elements(By.CLASS_NAME, '[data-testid="product-card"]')

print(f"{podushki=}")

parsed_data = []

for podushka in podushki:  # Проходим по каждому элементу podushki
    try:
        title = podushka.find_element(By.CSS_SELECTOR, '[itemprop="name"]').text
        price = podushka.find_element(By.CSS_SELECTOR, '[itemprop="price"]').get_attribute('content')
        link = podushka.find_element(By.CSS_SELECTOR, '[itemprop="url"]').get_attribute('href')
        parsed_data.append([title, price, link])

        # Добавляем данные в список
    except Exception as e:
        print("Произошла ошибка при парсинге:", e)

driver.quit()

# Сохранение данных в CSV файл
with open("podushki.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)

print("Данные сохранены в 'podushki.csv'")
