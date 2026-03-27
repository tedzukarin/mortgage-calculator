from flask import Flask, render_template

app = Flask(__name__)


# Единственный маршрут - главная страница
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Для разработки
    app.run(debug=True, host='0.0.0.0', port=5000)

    # Для продакшена закомментируйте строку выше и раскомментируйте эту:
    # app.run(host='0.0.0.0', port=5000)
