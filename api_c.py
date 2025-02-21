from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# URL для получения случайной цитаты
QUOTE_API_URL = "https://zenquotes.io/api/random"


@app.route("/")
def home():
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

    # HTML шаблон для отображения цитаты
    html = """
    <!doctype html>
    <html>
    <head>
        <title>Random Quote</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            blockquote { font-size: 1.5em; margin: 20px; }
            footer { text-align: right; font-size: 1.2em; color: #555; }
        </style>
    </head>
    <body>
        <h1>Случайная цитата</h1>
        <blockquote>
            <p>{{ quote }}</p>
            <footer>— {{ author }}</footer>
        </blockquote>
    </body>
    </html>
    """
    return render_template_string(html, quote=quote, author=author)


if __name__ == "__main__":
    app.run(debug=True)