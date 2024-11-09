from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    # Получаем текущие дату и время
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Возвращаем HTML, который отображает дату и время
    return f"<h1>Текущие дата и время: </h1><p>{formatted_time}</p>"


if __name__ == '__main__':
    app.run(debug=True)