#импортируем Flask и библиотеку Request
from flask import Flask, render_template, request
import requests

#импортируем объект класса Flask
app = Flask(__name__)

#формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
#создаем функцию с переменной weather, где мы будем сохранять погоду
def index():
   weather = None
   city = None

#формируем условия для проверки метода. Форму мы пока не создавали, но нам из неё необходимо будет взять только город.
   if request.method == 'POST':
#этот определенный город мы будем брать для запроса API
       city = request.form['city']
   weather = get_weather(city)
   return render_template("index.html", weather=weather)

#в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
   api_key = "fbab3316d08c77805b557662c44e51d6"
   #адрес, по которому мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ru&units=metric&lang='ru'"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()


def quotes():
   try:
      # Отправка GET-запроса к API
      response = requests.get(QUOTE_API_URL)
      response.raise_for_status()  # Проверка на наличие ошибок
      data = response.json()
      quote = data[0].get('q', 'No quote found')
      author = data[0].get('a', 'Unknown')
   except requests.exceptions.RequestException as e:
      quote = "Could not retrieve quote at this time."
      author = ""
      print(f"Error occurred: {e}")
   return quote, author

if __name__ == '__main__':
   app.run(debug=True)