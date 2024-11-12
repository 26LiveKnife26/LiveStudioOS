import requests
from bs4 import BeautifulSoup as bs

# Функция для отображения текстового браузера
def text_browser():
    # Запрашиваем ссылку у пользователя
    ssylka = input("Введите URL: ")
    if ssylka == "sear.":
        ssylka2 = input("Введите запрос: ")
        for i in ssylka2:
            if i == " ":
                ssylka2 += "+"
        url = f"https://www.google.com/search?client=firefox-b-lm&q={ssylka2}"
    url.strip()  # Удаляем пробелы из начала и конца
    url.encode("utf-8")

    try:
        # Отправляем GET-запрос на указанный URL
        response = requests.get(url)
        
        # Проверяем, что ответ успешный (статус код 200)
        response.raise_for_status()

        # Парсим HTML контент страницы
        tree = bs(response.text, 'html.parser')

        # Заголовок страницы
        title = tree.title.string if tree.title else 'Без заголовка'
        print(f"\nЗаголовок страницы: {title}\n")

        # Обрабатываем все ссылки на странице
        for link in tree.find_all('a'):
            href = link.get('href')
            text = link.text.strip()  # Также удаляем пробелы из текста ссылки
            if href:  # Проверка на существование атрибута href
                print(f"Содержимое: {text}")
                #print(f"Ссылка {href})

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск текстового браузера
if __name__ == "__main__":
    text_browser()