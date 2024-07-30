import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

link = "https://calorizator.ru/product/mushroom"  # Убедитесь, что URL указан правильно

driver.get(link)

time.sleep(5)

podushki = driver.find_elements(By.CLASS_NAME, 'even')

print(f"{podushki=}")

parsed_data = []

for podushka in podushki:  # Проходим по каждому элементу podushki
    try:
        title = podushka.find_element(By.CLASS_NAME, 'views-field-title').text
        price = podushka.find_element(By.CLASS_NAME, 'views-field-field-protein-value').text
        link = podushka.find_element(By.CLASS_NAME, 'views-field-title').get_attribute('href')
        parsed_data.append([title, price, link])

        # Добавляем данные в список
    except Exception as e:
        print("Произошла ошибка при парсинге:", e)

driver.quit()

# Сохранение данных в CSV файл
with open("podushki2.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)

print("Данные сохранены в 'podushki.csv'")
